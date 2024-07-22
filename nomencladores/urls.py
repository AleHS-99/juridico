from django.urls import path
from .views import *


urlpatterns = [
    path("t_contrato/",tContratoView.as_view(),name="t_contrato"),
    path("t_contrato/add/",addTcontrato.as_view(),name="add_t_contrato"),
    path("t_contrato/edit/<int:pk>/",updateTcontrato.as_view(),name="edit_t_contrato"),
    path("t_contrato/delete/<int:pk>/",deleteTcontrato.as_view(),name="delete_t_contrato"),
    path("f_pago/",fPagoView.as_view(),name="f_pago"),
    path("f_pago/add/",addfPago.as_view(),name="add_f_pago"),
    path("f_pago/edit/<int:pk>/",updatefPago.as_view(),name="edit_f_pago"),
    path("f_pago/delete//<int:pk>/",deletefPago.as_view(),name="delete_f_pago"),
        
    path("depart/",listDepart.as_view(),name="list_depart"),
    path("depart/add/",addDepart.as_view(),name="add_depart"),
    path("depart/edit/<int:pk>/",updateDepart.as_view(),name="edit_depart"),
    path("depart/delete/<int:pk>/",deleteDepart.as_view(),name="delete_depart"),
]