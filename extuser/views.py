from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
# Create your views here.
from .models import ExtUser


def index(request):
    users_list = ExtUser.objects.order_by('id').reverse()
    context = RequestContext(request, {
        'users_list': users_list,
    })
    return render(request, 'users.html', context)


def detail(request, user_id):
    user = get_object_or_404(ExtUser, id=user_id)
    return render(request, 'detail.html', {'user': user})


def register(request):
    return render(request, 'register.html')


def edit(request):
    return render(request, 'edit.html')


def login(request):
    return render(request, 'login.html')