from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',HomeView.as_view(),name='Home'),
    path('bar_data/',datos_barra,name='bar_data'),
    path('user/change/password',UserChangePassword.as_view(),name='change_password'),
    path('accounts/login/',LoginFormView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page="login"), name='logout')
]