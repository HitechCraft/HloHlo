
__author__ = 'Admin'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.LotAddView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.LotDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.LotUpdateView.as_view(), name='update'),
]