from django.urls import path
from .views import *


urlpatterns = [
    path("t_contrato/",tContratoView.as_view(),name="t_contrato"),
    path("t_contrato/add",addTcontrato.as_view(),name="add_t_contrato"),
    path("t_contrato/edit/<int:pk>/",updateTcontrato.as_view(),name="edit_t_contrato"),
    path("t_contrato/delete/<int:pk>/",deleteTcontrato.as_view(),name="delete_t_contrato"),
]