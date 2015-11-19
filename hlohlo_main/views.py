from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import LotAddForm, LotUpdateForm
from hlohlo_main.mixins import NoAuthenticated
from .models import Lot


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


def catalog(request):
    latest_lot_list = Lot.objects.order_by('-time_create')
    context = {'latest_lot_list': latest_lot_list}
    return render(request, 'lots/catalog.html', context)


def index(request):
    return render(request, 'index.html')


def detail(request, lot_id):

    lot = get_object_or_404(Lot, id=lot_id)
    return render(request, 'lots/detail.html', {'lot': lot})


