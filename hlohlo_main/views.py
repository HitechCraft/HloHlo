from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import LotAddForm, LotUpdateForm, CollectionForm
from hlohlo_main.mixins import NoAuthenticated
from .models import Lot, LotRater, Collection


class LotAddView(NoAuthenticated, generic.CreateView):
    model = Lot
    template_name = 'lots/add_lot.html'
    form_class = LotAddForm

    def get_success_url(self):
        return reverse('detail', kwargs={'lot_id': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(LotAddView, self).form_valid(form)


class LotUpdateView(generic.UpdateView):
    model = Lot
    template_name = 'lots/update_lot.html'
    form_class = LotUpdateForm

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'lot_id': self.get_object().id})


class LotDeleteView(generic.DeleteView):
    model = Lot
    template_name = 'lots/delete_lot.html'

    def get_success_url(self):
        return reverse_lazy('catalog')


class CollectionAddView(NoAuthenticated, generic.CreateView):
    model = Collection
    template_name = 'cols/add_col.html'
    form_class = CollectionForm

    def get_success_url(self):
        return reverse('col_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CollectionAddView, self).form_valid(form)


class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'cols/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        return context


class CollectionUpdateView(generic.UpdateView):
    model = Collection
    template_name = 'cols/update_col.html'
    form_class = CollectionForm

    def get_success_url(self):
        return reverse_lazy('col_detail', kwargs={'pk': self.get_object().id})


class CollectionDeleteView(generic.DeleteView):
    model = Collection
    template_name = 'cols/delete_col.html'

    def get_success_url(self):
        return reverse_lazy('cabinet')


def catalog(request):
    latest_lot_list = Lot.objects.order_by('-time_create')
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'lots/catalog.html', context)


def index(request):
    return render(request, 'index.html')


def redir(request):
    return redirect('catalog')


def uprate(request, lot_id):
    cur_lot = Lot.objects.get(id=lot_id)
    if 'rate_a' in request.POST and request.POST['rate_a']:
        if float(request.POST['rate']) > cur_lot.price:
            lot_rate = LotRater(lot=cur_lot, rate=float(request.POST['rate']), rater=request.user)
            lot_rate.save()
            cur_lot.price = float(request.POST['rate'])
            cur_lot.buyer = request.user
            cur_lot.save()
            request.session['success'] = 'Ставка сделана '
        else:
            request.session['errors'] = 'Ставка не может быть меньше или равна текущей цены '
    elif 'buy_now' in request.POST:
        cur_lot.buyer = request.user
        cur_lot.active = 0
        cur_lot.save()
        request.session['success'] = 'Вы успешно приобрели этот товар '
    else:
        request.session['errors'] = 'Ставка не может быть пустой '
    request.session['flag'] = 1

    return redirect('detail', lot_id=lot_id)


def detail(request, lot_id): #в будущем переписать этот костыль (ахаха смешно блядь) -_-
    lot = get_object_or_404(Lot, id=lot_id)
    lot.count_viewers += 1
    lot.save()
    if 'flag' in request.session:
        if request.session['flag'] == 1:
            request.session['flag'] = 2
            return render(request, 'lots/detail.html', {'lot': lot})
        else:
            if 'success' in request.session:
                del request.session['success']
            if 'errors' in request.session:
                del request.session['errors']
            return render(request, 'lots/detail.html', {'lot': lot})
    else:
        return render(request, 'lots/detail.html', {'lot': lot})


def archive(request, lot_id):
    lot = get_object_or_404(Lot, id=lot_id)
    lot.archived = True
    lot.save()
    return redirect('cabinet')
