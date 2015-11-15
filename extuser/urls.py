from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
               url(r'^profile/$', views.profile, name='profile'),
               url(r'^register/$', forms.RegisterFormView.as_view(), name='register'),
               url(r'^edit/$', forms.UserChangeFormView.as_view(), name='edit'),
               url(r'^login/$', forms.LoginFormView.as_view(), name='login'),
               url(r'^logout/$', forms.LogoutView.as_view(), name='logout'),
               ]
