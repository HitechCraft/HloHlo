from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
               url(r'^profile/$', views.profile, name='profile'),
               url(r'^cabinet/$', views.cabinet, name='cabinet'),
               url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
               url(r'^edit/$', views.UserChangeFormView.as_view(), name='edit'),
               url(r'^login/$', views.LoginFormView.as_view(), name='login'),
               url(r'^change_pass/$', views.UserChangePasswordView.as_view(), name='change_pass'),
               url(r'^change_avatar/$', views.AvatarChangeFormView.as_view(), name='change_avatar'),
               url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
               ]
