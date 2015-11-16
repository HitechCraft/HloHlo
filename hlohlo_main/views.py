from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .forms import LotAddForm
from hlohlo_main.mixins import NoAuthenticated
from .models import Lot


class LotAddView(NoAuthenticated, generic.CreateView):
    model = Lot

    template_name = 'lots/add_lot.html'
    form_class = LotAddForm

    success_url = reverse_lazy('detail', kwargs={'lot_id': model.objects.last().id + 1})

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(LotAddView, self).form_valid(form)


def index(request):

    latest_lot_list = Lot.objects.order_by('-time_create')
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'lots/index.html', context)


def detail(request, lot_id):

    lot = get_object_or_404(Lot, id=lot_id)
    return render(request, 'lots/detail.html', {'lot': lot})


