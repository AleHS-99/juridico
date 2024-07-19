from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/',listContrato.as_view(),name='listContratoU'),
    path('Add/<int:pk>/',addContrato.as_view(),name='addContratoU'),
    path('Edit/<int:pk>/<int:dp>/',updateContrato.as_view(),name='updateContratoU'),
    path('Delete/<int:pk>/<int:dp>/',deleteContrato.as_view(),name='deleteContratoU'),
]