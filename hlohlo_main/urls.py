__author__ = 'Admin'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^add/$', views.AddLotView.as_view(), name='add'),
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<lot_id>[0-9]+)/add/$', views.add_lot, name='add_lot'),
    # ex: /polls/5/vote/
    #url(r'^(?P<lot_id>[0-9]+)/vote/$', views.vote, name='vote'),
]