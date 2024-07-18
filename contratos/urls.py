from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/',listContrato.as_view(),name='listContratoU'),
    path('Add/<int:pk>/',addContrato.as_view(),name='addContratoU'),
]