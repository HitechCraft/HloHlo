
__author__ = 'Admin'

from django.conf.urls import url, include

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.redir, name='redir'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^col/add/$', views.CollectionAddView.as_view(), name='col_add'),
    url(r'^col/(?P<pk>[0-9]+)/$', views.CollectionDetailView.as_view(), name='col_detail'),
    url(r'^col/(?P<pk>[0-9]+)/update/$', views.CollectionUpdateView.as_view(), name='col_update'),
    url(r'^col/(?P<pk>[0-9]+)/delete/$', views.CollectionDeleteView.as_view(), name='col_delete'),
    url(r'^(?P<lot_id>[0-9]+)/uprate/$', views.uprate, name='uprate'),
    url(r'^add/$', views.LotAddView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.LotDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.LotUpdateView.as_view(), name='update'),
    url(r'^(?P<lot_id>[0-9]+)/archive/$', views.archive, name='archive'),
]