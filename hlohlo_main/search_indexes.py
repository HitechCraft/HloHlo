import datetime
from haystack import indexes
from hlohlo_main.models import Lot
from django.utils import timezone


class LotIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Lot

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(time_create__lte=timezone.now())

