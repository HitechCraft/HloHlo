<<<<<<< HEAD
__author__ = 'Admin'

=======
>>>>>>> 3333cda9b2aff3f4602bd59339cca8bd8d2f1400
from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    # ex: /polls/
    url(r'^add/$', views.AddLotView.as_view(), name='add'),
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<lot_id>[0-9]+)/add/$', views.add_lot, name='add_lot'),
    # ex: /polls/5/vote/
    #url(r'^(?P<lot_id>[0-9]+)/vote/$', views.vote, name='vote'),
=======
    url(r'^$', views.index, name='index'),
>>>>>>> 3333cda9b2aff3f4602bd59339cca8bd8d2f1400
]