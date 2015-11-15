
__author__ = 'Admin'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.LotAddView.as_view(), name='add'),
]