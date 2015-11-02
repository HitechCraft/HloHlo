from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import AddLotForm
from .models import Lot
# Create your views here.


class AddLotView(generic.CreateView):

    model = Lot
    template_name = 'lots/add_lot.html'
    form_class = AddLotForm


def index(request):

    latest_lot_list = Lot.objects.order_by('-time_create')
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'lots/index.html', context)


def detail(request, lot_id):

    lot = get_object_or_404(Lot, id=lot_id)
    return render(request, 'lots/detail.html', {'lot': lot})

"""
def add_lot(request):

    return render(request, 'lots/add_lot.html')
"""