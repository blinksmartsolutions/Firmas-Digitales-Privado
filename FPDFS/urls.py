from django.urls import path
from . import views

urlpatterns = [
    path("sign_pdf/<int:id_PDF>", views.sign_pdf, name="sign_pdf"),
    path("", views.dashboard, name="dashboard"),
    path(
        "cargar-pdf/<int:id>",
        views.cargarpdfUsuarioGeneral,
        name="cargarpdfUsuarioGeneral",
    ),  # enviar documentos de futuros Innovadores
    path(
        "cargar-solicitud-de-orden-de-compras/<int:id>",
        views.cargarpdfsolicitudordencompras,
        name="cargarpdfsolicitudordencompras",
    ),  # enviar documentos de futuros Innovadores
    path(
        "cargar-ordendecompra/<int:id>",
        views.cargarpdfOrdendeCompra,
        name="cargarpdfOrdendeCompra",
    ),  # enviar documentos de futuros Innovadores
    path(
        "cambiarEstatusPdf/<int:id_PDF>",
        views.cambiarEstatusPdf,
        name="cambiarEstatusPdf",
    ),
    path(
        "AlmacencambiarEstatusPdf/<int:id_PDF>",
        views.AlmacencambiarEstatusPdf,
        name="AlmacencambiarEstatusPdf",
    ),
    path(
        "AlmacenestatusAceptadoPdf/<int:id_PDF>",
        views.AlmacenestatusAceptadoPdf,
        name="AlmacenestatusAceptadoPdf",
    ),
    path(
        "socgccambiarEstatusPdf/<int:id_PDF>",
        views.socgccambiarEstatusPdf,
        name="socgccambiarEstatusPdf",
    ),
    path(
        "ordencomprasgerentecambiarEstatusPdf/<int:id_PDF>",
        views.ordencomprasgerentecambiarEstatusPdf,
        name="ordencomprasgerentecambiarEstatusPdf",
    ),
    path(
        "EliminarpdfUsuarioGeneral/<int:id_PDF>",
        views.EliminarpdfUsuarioGeneral,
        name="EliminarpdfUsuarioGeneral",
    ),
    path("save_signature/<int:id_PDF>", views.save_signature, name="save_signature"),
]
