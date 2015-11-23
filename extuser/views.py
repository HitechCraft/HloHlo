from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.views import generic
from hlohlo_main.mixins import Authenticated, NoAuthenticated
# Create your views here.
from django.views.generic import FormView
from extuser.forms import LoginForm, UserCreationForm, UserChangeForm, UserChangePasswordForm
from hlohlo_main.models import Lot, Collection
from .models import ExtUser


class LoginFormView(Authenticated, FormView):
    form_class = LoginForm
    success_url = reverse_lazy('cabinet')
    template_name = "login.html"

    def form_valid(self, form):
        form.login(self.request)

        return super(LoginFormView, self).form_valid(form)


class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return redirect('login')


class RegisterFormView(Authenticated, FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = reverse_lazy('login')

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class UserChangeFormView(NoAuthenticated, generic.UpdateView):
    model = ExtUser
    form_class = UserChangeForm
    template_name = "edit.html"

    def get_object(self):
        return get_object_or_404(ExtUser, pk=self.request.user.id)

    """def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        self.object = ExtUser.objects.get(id=self.request.user.id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
        """

    def get_success_url(self):
        return reverse_lazy('profile')


class UserChangePasswordView(NoAuthenticated, generic.UpdateView):
    model = ExtUser
    form_class = UserChangePasswordForm
    template_name = "change_pass.html"

    def get_object(self):
        return get_object_or_404(ExtUser, pk=self.request.user.id)

    def get_success_url(self):
        return reverse_lazy('profile')


def index(request):
    users_list = ExtUser.objects.order_by('id').reverse()
    context = RequestContext(request, {
        'users_list': users_list,
    })
    return render(request, 'users.html', context)


def detail(request, user_id):
    user = get_object_or_404(ExtUser, id=user_id)
    return render(request, 'detail.html', {'user': user})


def profile(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        return render(request, 'profile.html', {'user': request.user})


def cabinet(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        lot_cols = Collection.objects.filter(author=request.user).order_by('-id')
        my_lots = Lot.objects.filter(author=request.user).order_by('-time_create')
        lot_arch_s = Lot.objects.filter(author=request.user, archived=True)\
            .order_by('-time_create')
        lot_arch_b = Lot.objects.filter(buyer=request.user, archived=True)\
            .order_by('-time_create')
        lot_cart = Lot.objects.filter(buyer=request.user, active=False, archived=False).order_by('-time_create')
        lot_fav = Lot.objects.filter(buyer=request.user, active=True).order_by('-time_create')
        return render(request, 'cabinet.html', {'user': request.user, 'lot_cart': lot_cart, 'lot_fav': lot_fav,
                                                'my_lots': my_lots, 'lot_arch_s': lot_arch_s, 'lot_arch_b': lot_arch_b,
                                                'lot_cols': lot_cols})
