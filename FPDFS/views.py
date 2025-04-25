# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

# auth
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin


from django.db.models import Q

from .forms import cargarpdfUsuarioGeneralform


from .forms import cargarpdfOrdendeCompraform


from .forms import cargarpdfsolicitudordencomprasform


from users.models import UsuariosTrime


from FPDFS.models import pdfEnviadosGerente
from FPDFS.models import pdfEnviadosAlmacen
from FPDFS.models import pdfEnviadosCompras

from FPDFS.models import pdf2EnviadoGGeneral
from FPDFS.models import solicitudOrdendeCompras


from .forms import cambiarEStatuspdfUsuarioGeneralform
from .forms import cambiarEStatuspdfolicitudordencomprasform

from .forms import cambiarEStatuspdfordencomprasform


pdf_file_path = "./FPDFS/templates/Contrato.pdf"


def user_is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@xframe_options_sameorigin
@login_required()
def sign_pdf(request, id_PDF):

    user_id = request.user.id

    if user_is_in_group(request.user, "GERENCIA GENERAL"):

        requisiciones_enviadas = pdf2EnviadoGGeneral.objects.filter(id=id_PDF)

        # Contenido para administradores
        context = {
            "message": "Contenido exclusivo para administradores",
            "requisiciones_enviadas": requisiciones_enviadas,
            "user_id": user_id,
        }
    elif user_is_in_group(request.user, "GERENTE"):

        requisiciones_enviadas = pdfEnviadosGerente.objects.filter(id=id_PDF)

        # Contenido para usuarios básicos
        context = {
            "message": "Contenido para usuarios básicos",
            "requisiciones_enviadas": requisiciones_enviadas,
            "user_id": user_id,
        }

    elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE ALMACEN"):

        requisiciones_enviadas = solicitudOrdendeCompras.objects.filter(id=id_PDF)

        context = {
            "message": "Contenido para usuarios básicos",
            "requisiciones_enviadas": requisiciones_enviadas,
            "user_id": user_id,
        }

    elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE COMPRAS"):

        requisiciones_enviadas = pdf2EnviadoGGeneral.objects.filter(id=id_PDF)

        # Contenido para usuarios básicos
        context = {
            "message": "Contenido para usuarios básicos",
            "requisiciones_enviadas": requisiciones_enviadas,
            "user_id": user_id,
        }

    else:
        # Contenido para otros usuarios o visitantes
        context = {
            "message": "Contenido para otros usuarios",
            "requisiciones_enviadas": requisiciones_enviadas,
            "user_id": user_id,
        }

    return render(request, "paginas/index.html", context)


DOCUMENTOS = ["Requisiciones", "Cotizaciones", "Ordenes de Compra"]


@login_required()
@xframe_options_sameorigin
def dashboard(request):

    if user_is_in_group(request.user, "GERENCIA GENERAL"):
        ordenes_compra_enviadas = pdf2EnviadoGGeneral.objects.filter(
            Q(ESTATUS_DOCUMENTO="Rechazado por GG")
            | Q(ESTATUS_DOCUMENTO="Firmado por GG")
            | Q(ESTATUS_DOCUMENTO="Rechazado por GG")
            | Q(ESTATUS_DOCUMENTO="Firmado por Compras")
        ).all()
        ordenes_compra_enviadas_N = ordenes_compra_enviadas.filter(
            ESTATUS_DOCUMENTO="Firmado por Compras"
        )
        ordenes_compra_enviadas_F = ordenes_compra_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Firmado por GG")
        )
        ordenes_compra_enviadas_R = ordenes_compra_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Rechazado por GG")
        )

        # Contenido para administradores
        context = {
            "ordenes_compra_enviadas": ordenes_compra_enviadas,
            "ordenes_compra_enviadas_N": ordenes_compra_enviadas_N,
            "ordenes_compra_enviadas_F": ordenes_compra_enviadas_F,
            "ordenes_compra_enviadas_R": ordenes_compra_enviadas_R,
            "message": "Contenido exclusivo para GERENTE GENERAL",
            "documento": 3,
        }
        messages.success(
            request, f"Hola {request.user}, Contenido exclusivo para GERENTE GENERAL"
        )

    elif user_is_in_group(request.user, "DEPARTAMENTO DE ADMINISTRACION"):
        ordenes_compra_enviadas = pdf2EnviadoGGeneral.objects.all()
        # Contenido para usuarios básicos
        context = {
            "ordenes_compra_enviadas": ordenes_compra_enviadas,
            "message": "Contenido para GERENTE DEL DEPARTAMENTO DE ADMINISTRACION",
            "documento": 3,
        }
        messages.success(
            request,
            f"Hola {request.user}, Contenido exclusivo para GERENTE DEL DEPARTAMENTO DE ADMINISTRACION",
        )

    ## =============================== REQUISICIONES ===============================

    elif user_is_in_group(request.user, "USUARIO GENERAL"):

        # falta filtrar por usuario.
        id_user = request.user.id
        requisiciones_enviadas = pdfEnviadosGerente.objects.filter(usuario=id_user)
        requisiciones_enviadas_N = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="ENVIADO"
        )
        requisiciones_enviadas_F = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="FIRMADO"
        )
        requisiciones_enviadas_R = requisiciones_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Rechazado por Almacen")
            | Q(ESTATUS_DOCUMENTO="Rechazado por Gerente")
        )
        requisiciones_enviadas_A = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="Aceptado por Almacen"
        )
        # PUEDE CARGAR DOCUMENTO PDF Y ENVIAR A GERENTE LA REQUISICION
        # Contenido para usuarios básicos
        context = {
            "requisiciones_enviadas": requisiciones_enviadas,
            "requisiciones_enviadas_N": requisiciones_enviadas_N,
            "requisiciones_enviadas_F": requisiciones_enviadas_F,
            "requisiciones_enviadas_R": requisiciones_enviadas_R,
            "requisiciones_enviadas_A": requisiciones_enviadas_A,
            "message": "Contenido para usuarios básicos",
            "documento": 1,
            "id": id_user,
        }
        messages.success(
            request, f"Hola {request.user}, Contenido exclusivo para usuarios básicos"
        )

    elif user_is_in_group(request.user, "GERENTE"):
        # VE LOS DOCUMENTOS DE REQUISICIONES ENVIADO POR EL USUARIO GENERAL
        # SI ACEPTA, FIRMA Y SE ENVIA A ALMACEN
        # SI RECHAZA SE CAMBIA DE ESTATUS A RECHAZADO
        # Contenido para usuarios básicos

        requisiciones_enviadas = pdfEnviadosGerente.objects.filter(
            usuario__Departamento_Usuario=request.user.Departamento_Usuario
        ).all()

        requisiciones_enviadas_N = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="ENVIADO"
        )
        requisiciones_enviadas_F = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="FIRMADO"
        )
        requisiciones_enviadas_R = requisiciones_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Rechazado por Almacen")
            | Q(ESTATUS_DOCUMENTO="Rechazado por Gerente")
        )
        requisiciones_enviadas_A = requisiciones_enviadas.filter(
            ESTATUS_DOCUMENTO="Aceptado por Almacen"
        )

        context = {
            "requisiciones_enviadas": requisiciones_enviadas,
            "requisiciones_enviadas_N": requisiciones_enviadas_N,
            "requisiciones_enviadas_F": requisiciones_enviadas_F,
            "requisiciones_enviadas_R": requisiciones_enviadas_R,
            "requisiciones_enviadas_A": requisiciones_enviadas_A,
            "message": "Contenido para GERENTE",
            "documento": 1,
        }
        messages.success(
            request, f"Hola {request.user}, contenido exclusivo para GERENTE"
        )

    elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE ALMACEN"):

        requisiciones_enviadas = pdfEnviadosAlmacen.objects.all()
        requisiciones_enviadas_N = requisiciones_enviadas.filter(
            documento_pdf__ESTATUS_DOCUMENTO="ENVIADO"
        )
        requisiciones_enviadas_F = requisiciones_enviadas.filter(
            documento_pdf__ESTATUS_DOCUMENTO="FIRMADO"
        )
        requisiciones_enviadas_R = requisiciones_enviadas.filter(
            documento_pdf__ESTATUS_DOCUMENTO="Rechazado por Almacen"
        )
        requisiciones_enviadas_A = requisiciones_enviadas.filter(
            documento_pdf__ESTATUS_DOCUMENTO="Aceptado por Almacen"
        )

        solicitud_ordenes_compras_enviadas = solicitudOrdendeCompras.objects.all()

        solicitud_ordenes_compras_enviadas_N = (
            solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO="ENVIADO")
        )
        solicitud_ordenes_compras_enviadas_F = (
            solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO="FIRMADO")
        )
        solicitud_ordenes_compras_enviadas_R = (
            solicitud_ordenes_compras_enviadas.filter(
                Q(ESTATUS_DOCUMENTO="Rechazado por Almacen")
                | Q(ESTATUS_DOCUMENTO="Rechazado por Compras")
            )
        )

        # VE LOS DOCUMENTOS DE REQUISICIONES ENVIADO POR EL GERENTE
        # VERIFICA EXISTENCIA. SI HAY, ACEPTA, FIRMA Y SE CAMBIA DE ESTATUS A ACEPTADO
        # SI RECHAZA SE CAMBIA DE ESTATUS A RECHAZADO, SE FIRMA Y SE ENVIA A DEPARTAMENTO DE COMPRAS
        # Contenido para usuarios básicos
        context = {
            "requisiciones_enviadas": requisiciones_enviadas,
            "requisiciones_enviadas_N": requisiciones_enviadas_N,
            "requisiciones_enviadas_F": requisiciones_enviadas_F,
            "requisiciones_enviadas_R": requisiciones_enviadas_R,
            "requisiciones_enviadas_A": requisiciones_enviadas_A,
            "solicitud_ordenes_compras_enviadas": solicitud_ordenes_compras_enviadas,
            "solicitud_ordenes_compras_enviadas_N": solicitud_ordenes_compras_enviadas_N,
            "solicitud_ordenes_compras_enviadas_F": solicitud_ordenes_compras_enviadas_F,
            "solicitud_ordenes_compras_enviadas_R": solicitud_ordenes_compras_enviadas_R,
            "message": "Contenido para GERENTE DE DEPARTAMENTO DE ALMACEN",
            "documento": 5,
        }
        messages.success(
            request,
            f"Hola {request.user}, Contenido exclusivo para GERENTE DE DEPARTAMENTO DE ALMACEN",
        )

    elif user_is_in_group(request.user, "DEPARTAMENTO DE ALMACEN"):
        # Contenido para usuarios básicos

        requisiciones_enviadas = pdfEnviadosAlmacen.objects.all()

        solicitud_ordenes_compras_enviadas = solicitudOrdendeCompras.objects.all()
        solicitud_ordenes_compras_enviadas_N = (
            solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO="ENVIADO")
        )
        solicitud_ordenes_compras_enviadas_F = (
            solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO="FIRMADO")
        )
        solicitud_ordenes_compras_enviadas_R = (
            solicitud_ordenes_compras_enviadas.filter(
                ESTATUS_DOCUMENTO="Rechazado por Almacen"
            )
        )

        context = {
            "requisiciones_enviadas": requisiciones_enviadas,
            "solicitud_ordenes_compras_enviadas": solicitud_ordenes_compras_enviadas,
            "solicitud_ordenes_compras_enviadas_N": solicitud_ordenes_compras_enviadas_N,
            "solicitud_ordenes_compras_enviadas_F": solicitud_ordenes_compras_enviadas_F,
            "solicitud_ordenes_compras_enviadas_R": solicitud_ordenes_compras_enviadas_R,
            "message": "Contenido para usuarios DEL DEPARTAMENTO DE ALMACEN",
            "documento": 5,
        }
        messages.success(
            request,
            f"Hola {request.user}, Contenido exclusivo para usuarios DEL DEPARTAMENTO DE ALMACEN",
        )

    ### ===================== ORDENES DE COMPRAS Y COTIZACIONES ===============================

    elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE COMPRAS"):
        ## VE DOCUMENTO DE REQUISICION ENVIADO POR ALAMCEN
        # CREA ORDEN PARA QUE LOS USUARIOS BASICOS DEL DEPARTAMENTO DE COMPRAS CARGUEN LAS COTIZACIONES
        # VE LAS COTIZACIONES CARGADAS HASTA ACEPTAR. AL ACEPTARLA SE DA OPCION PARA CARGAR ORDEN DE COMPRA, FIRMARLA Y ENVIARLA AL GERENTE GENERAL
        # Contenido para usuarios básicos

        solicitud_ordenes_compras_enviadas = (
            solicitudOrdendeCompras.objects.all().exclude(
                Q(ESTATUS_DOCUMENTO="ENVIADO")
                | Q(ESTATUS_DOCUMENTO="Rechazado por Almacen")
            )
        )
        # solicitud_ordenes_compras_enviadas_N = solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO='ENVIADO')
        solicitud_ordenes_compras_enviadas_F = (
            solicitud_ordenes_compras_enviadas.filter(ESTATUS_DOCUMENTO="FIRMADO")
        )
        solicitud_ordenes_compras_enviadas_R = (
            solicitud_ordenes_compras_enviadas.filter(
                ESTATUS_DOCUMENTO="Rechazado por Compras"
            )
        )

        # ordenes de compras  cargada por el gerente de compras
        ordenes_compra_enviadas = pdf2EnviadoGGeneral.objects.all().order_by(
            "-fecha_modificacion"
        )  # ordenes de compras enviados

        ordenes_compra_enviadas_N = ordenes_compra_enviadas.filter(
            ESTATUS_DOCUMENTO="ENVIADO"
        )
        ordenes_compra_enviadas_F = ordenes_compra_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Firmado por GG")
            | Q(ESTATUS_DOCUMENTO="Firmado por Compras")
        )
        ordenes_compra_enviadas_R = ordenes_compra_enviadas.filter(
            Q(ESTATUS_DOCUMENTO="Rechazado por GG")
            | Q(ESTATUS_DOCUMENTO="Rechazado por Compras")
        )

        context = {
            "solicitud_ordenes_compras_enviadas": solicitud_ordenes_compras_enviadas,
            # "solicitud_ordenes_compras_enviadas_N": solicitud_ordenes_compras_enviadas_N,
            "solicitud_ordenes_compras_enviadas_F": solicitud_ordenes_compras_enviadas_F,
            "solicitud_ordenes_compras_enviadas_R": solicitud_ordenes_compras_enviadas_R,
            "ordenes_compra_enviadas": ordenes_compra_enviadas,
            "ordenes_compra_enviadas_N": ordenes_compra_enviadas_N,
            "ordenes_compra_enviadas_F": ordenes_compra_enviadas_F,
            "ordenes_compra_enviadas_R": ordenes_compra_enviadas_R,
            "message": "Contenido para GERENTE DE DEPARTAMENTO DE COMPRAS",
            "documento": 4,
        }
        messages.success(
            request,
            f"Hola {request.user}, Contenido exclusivo para GERENTE DE DEPARTAMENTO DE COMPRAS",
        )

    elif user_is_in_group(request.user, "DEPARTAMENTO DE COMPRAS"):
        # VE LA ORDEN DE REQUISICION Y LA ORDEN DE COMPRA GENERADA POR EL GERENTE DE COMPRAS
        # CARGA LAS COTIZACIONES PARAR ENVIARLA AL GERENTE DE COMPRAS.
        # Contenido para usuarios básicos

        solicitud_ordenes_compras_enviadas = solicitudOrdendeCompras.objects.filter(
            ESTATUS_DOCUMENTO="FIRMADO"
        ).all()

        context = {
            "message": "Contenido para usuarios DEL DEPARTAMENTO DE COMPRAS",
            "documento": 2,
            "solicitud_ordenes_compras_enviadas": solicitud_ordenes_compras_enviadas,
        }
        messages.success(
            request,
            f"Hola {request.user}, Contenido exclusivo para usuarios DEL DEPARTAMENTO DE COMPRAS",
        )

    else:
        # Contenido para otros usuarios o visitantes
        context = {"message": "Contenido para otros usuarios"}
        messages.success(
            request, f"Hola {request.user}, contenido exclusivo para otros usuarios"
        )

    return render(request, "paginas/dashboard.html", context)


## formulario para cargar el pdf, en este caso para el gerente
@login_required()
def cargarpdfUsuarioGeneral(request, id):
    username = request.user

    user_id = UsuariosTrime.objects.get(id=id)
    if request.method == "POST":
        formulario = cargarpdfUsuarioGeneralform(request.POST, request.FILES)
        if formulario.is_valid():

            usuario = user_id
            documento_pdf = request.FILES["documento_pdf"]
            nombre_documento = request.POST["nombre_documento"]
            N_documento = request.POST["N_documento"]
            descripcion_documento = request.POST["descripcion_documento"]

            Archivos = pdfEnviadosGerente.objects.create(
                usuario=user_id,
                documento_pdf=documento_pdf,
                nombre_documento=nombre_documento,
                N_documento=N_documento,
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha cargado el PDF correctamente!")
            return redirect("dashboard")
    else:
        formulario = cargarpdfUsuarioGeneralform()

    context = {"formulario": formulario}

    return render(request, "paginas/formulario_carga_pdf.html", context)


## formulario para cargar el pdf, en este caso para el gerente
@login_required()
def cargarpdfsolicitudordencompras(request, id):
    user_id = request.user.id

    user_id = UsuariosTrime.objects.get(id=user_id)
    requisicioncancelad_id = pdfEnviadosAlmacen.objects.get(id=id)

    if request.method == "POST":
        formulario = cargarpdfsolicitudordencomprasform(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = user_id
            documento_pdf = request.FILES["documento_pdf"]
            nombre_documento = request.POST["nombre_documento"]
            N_documento = request.POST["N_documento"]
            descripcion_documento = request.POST["descripcion_documento"]

            Archivos = solicitudOrdendeCompras.objects.create(
                usuario=user_id,
                documento_pdf=documento_pdf,
                requisicionCancelada=requisicioncancelad_id,
                nombre_documento=nombre_documento,
                N_documento=N_documento,
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha cargado el PDF correctamente!")
            return redirect("dashboard")
    else:
        formulario = cargarpdfsolicitudordencomprasform()

    context = {"formulario": formulario}

    return render(request, "paginas/formulario_carga_pdf.html", context)


@login_required()
def cargarpdfOrdendeCompra(request, id):
    user_id = request.user.id

    user_id = UsuariosTrime.objects.get(id=user_id)
    cotizacionAcecptada_id = solicitudOrdendeCompras.objects.get(id=id)

    if request.method == "POST":
        formulario = cargarpdfOrdendeCompraform(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = user_id
            documento_pdf = request.FILES["documento_pdf"]
            nombre_documento = request.POST["nombre_documento"]
            N_documento = request.POST["N_documento"]
            descripcion_documento = request.POST["descripcion_documento"]

            Archivos = pdf2EnviadoGGeneral.objects.create(
                usuario=user_id,
                documento_pdf=documento_pdf,
                cotizacionAcecptada=cotizacionAcecptada_id,
                nombre_documento=nombre_documento,
                N_documento=N_documento,
                descripcion_documento=descripcion_documento,
            )

            PDF_CAMBIAR_ESTATUS = solicitudOrdendeCompras.objects.filter(id=id).update(
                ESTATUS_DOCUMENTO="Generada ODC"
            )

            messages.success(request, "¡Se ha cargado el PDF correctamente!")
            return redirect("dashboard")
    else:
        formulario = cargarpdfOrdendeCompraform()

    context = {"formulario": formulario}

    return render(request, "paginas/formulario_carga_pdf.html", context)


## CAMBIAR ESTATUS DEL PDF REQUISICION
@login_required()
def cambiarEstatusPdf(request, id_PDF):

    pdf = pdfEnviadosGerente.objects.get(id=id_PDF)

    formulario = cambiarEStatuspdfUsuarioGeneralform(request.POST or None, instance=pdf)

    if formulario.is_valid():
        descripcion_documento = request.POST["descripcion_documento"]

        PDF_CAMBIAR_ESTATUS = pdfEnviadosGerente.objects.filter(id=id_PDF).update(
            ESTATUS_DOCUMENTO="Rechazado por Gerente",
            descripcion_documento=descripcion_documento,
        )

        messages.success(request, "¡Se ha modificado el PDF correctamente!")
        return redirect("dashboard")

    return render(
        request, "paginas/formulario_carga_pdf.html", {"formulario": formulario}
    )


## CAMBIAR ESTATUS DEL PDF DE SOLICITUD DE ORDENES DE COMPRA
@login_required()
def socgccambiarEstatusPdf(request, id_PDF):

    pdf = solicitudOrdendeCompras.objects.get(id=id_PDF)

    formulario = cambiarEStatuspdfolicitudordencomprasform(
        request.POST or None, instance=pdf
    )

    if formulario.is_valid():
        descripcion_documento = request.POST["descripcion_documento"]

        if user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE COMPRAS"):
            PDF_CAMBIAR_ESTATUS = solicitudOrdendeCompras.objects.filter(
                id=id_PDF
            ).update(
                ESTATUS_DOCUMENTO="Rechazado por Compras",
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha modificado el PDF correctamente!")
            return redirect("dashboard")

        elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE ALMACEN"):
            PDF_CAMBIAR_ESTATUS = solicitudOrdendeCompras.objects.filter(
                id=id_PDF
            ).update(
                ESTATUS_DOCUMENTO="Rechazado por Almacen",
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha modificado el PDF correctamente!")
            return redirect("dashboard")

    return render(
        request, "paginas/formulario_carga_pdf.html", {"formulario": formulario}
    )


## CAMBIAR ESTATUS DEL PDF ORDEN DE COMPRAS
@login_required()
def ordencomprasgerentecambiarEstatusPdf(request, id_PDF):

    pdf = pdf2EnviadoGGeneral.objects.get(id=id_PDF)

    formulario = cambiarEStatuspdfordencomprasform(request.POST or None, instance=pdf)

    if formulario.is_valid():
        descripcion_documento = request.POST["descripcion_documento"]

        if user_is_in_group(request.user, "GERENCIA GENERAL"):
            PDF_CAMBIAR_ESTATUS = pdf2EnviadoGGeneral.objects.filter(id=id_PDF).update(
                ESTATUS_DOCUMENTO="Rechazado por GG",
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha modificado el PDF correctamente!")
            return redirect("dashboard")

        elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE COMPRAS"):
            PDF_CAMBIAR_ESTATUS = pdf2EnviadoGGeneral.objects.filter(id=id_PDF).update(
                ESTATUS_DOCUMENTO="Rechazado por Compras",
                descripcion_documento=descripcion_documento,
            )

            messages.success(request, "¡Se ha modificado el PDF correctamente!")
            return redirect("dashboard")

    return render(
        request, "paginas/formulario_carga_pdf.html", {"formulario": formulario}
    )


## CAMBIAR ESTATUS DE PDF
@login_required()
def AlmacencambiarEstatusPdf(request, id_PDF):
    pdf = pdfEnviadosGerente.objects.get(id=id_PDF)
    formulario = cambiarEStatuspdfUsuarioGeneralform(request.POST or None, instance=pdf)

    if formulario.is_valid():
        descripcion_documento = request.POST["descripcion_documento"]

        PDF_CAMBIAR_ESTATUS = pdfEnviadosGerente.objects.filter(id=id_PDF).update(
            ESTATUS_DOCUMENTO="Rechazado por Almacen",
            descripcion_documento=descripcion_documento,
        )

        messages.success(request, "¡Se ha modificado el PDF correctamente!")
        return redirect("dashboard")

    return render(
        request, "paginas/formulario_carga_pdf.html", {"formulario": formulario}
    )


## CAMBIAR ESTATUS DE PDF
@login_required()
def AlmacenestatusAceptadoPdf(request, id_PDF):

    PDF_CAMBIAR_ESTATUS = pdfEnviadosGerente.objects.filter(id=id_PDF).update(
        ESTATUS_DOCUMENTO="Aceptado por Almacen"
    )

    messages.success(request, "¡Se ha modificado el PDF correctamente!")
    return redirect("dashboard")


@login_required()
def EliminarpdfUsuarioGeneral(request, id_PDF):
    PDF_CAMBIAR_ESTATUS = pdfEnviadosGerente.objects.filter(id=id_PDF).delete()

    messages.success(request, "¡PDF eliminado correctamente!")
    return redirect("dashboard")


from django.core.files import File
from django.core.files.base import ContentFile
import os


def procesarfirma(pdf_path, firma_path, x_pdf, y_pdf):
    import fitz  # PyMuPDF
    from PIL import Image

    try:
        # Step 1: Open the existing PDF
        # pdf_document = fitz.open("media/docfirmas_1.PDF")  # Replace with your PDF file

        pdf_document = fitz.open("media/" + pdf_path)

        print(pdf_document)

        # Step 2: Select the page where you want to add the image (0-indexed)
        page_number1 = 0  # First page
        page_number2 = 3  # First page

        page = pdf_document[page_number1]
        # page2 = pdf_document[page_number2]

        # Step 3: Load the image
        # image = Image.open("media/Firma.png")

        image = Image.open("media/" + firma_path)

        # Step 4: Convert to RGBA (if not already in that mode)
        image = image.convert("RGBA")

        # Step 5: Create a new image with transparency
        data = image.getdata()

        # Step 6: Modify the alpha channel to make white background transparent
        new_data = []
        for item in data:
            # Change all white (also shades of whites)
            if item[0] in list(range(200, 256)):  # R
                if item[1] in list(range(200, 256)):  # G
                    if item[2] in list(range(200, 256)):  # B
                        new_data.append((255, 255, 255, 0))  # Change to transparent
                    else:
                        new_data.append(item)  # Keep original
                else:
                    new_data.append(item)  # Keep original
            else:
                new_data.append(item)  # Keep original

        # Step 7: Update image data
        image.putdata(new_data)

        # Step 8: Save the new image
        image.save("transparent_image.png", "PNG")

        image_file = "transparent_image.png"

        #
        # position = (500, 570)  # (x, y) coordinates in points

        position = (x_pdf, y_pdf)  # (x, y) coordinates in points

        new_width = 100  # New width in points
        new_height = 100  # New height in points

        # Step 9: Insert the image with the new size
        page.insert_image(
            fitz.Rect(
                position[0],
                position[1],
                position[0] + new_width,
                position[1] + new_height,
            ),
            filename=image_file,
        )

        # Step 10: Insert the image with the new size
        # page2.insert_image(fitz.Rect(position[0], position[1], position[0] + new_width, position[1] + new_height),
        #                filename=image_file)

        # Step 11: Save the modified PDF
        print("paso11")
        # modified_pdf_path ="media/modified_example.pdf"

        modified_pdf_path = "media/" + pdf_path[:-4] + "_modificated.pdf"

        print(modified_pdf_path)
        pdf_document.save(modified_pdf_path)  # Save as a new file or overwrite

        # Step 12: Save the modified PDF to the database
        # with open(modified_pdf_path, 'rb') as f:
        #     modified_pdf_instance = Signature()
        #     modified_pdf_instance.pdf_file_firmado.save(os.path.basename(modified_pdf_path), File(f))
        #     modified_pdf_instance.save()

        return modified_pdf_path

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the PDF is closed if it was opened
        try:
            pdf_document.close()
        except:
            pass


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import re
from .models import Signature

# @csrf_exempt  # Use this only for testing; consider using CSRF tokens in production
# def save_signature(request):
#     if request.method == 'POST':
#         data = request.POST.get('image')


#         # Remove the header from the data URL
#         image_data = re.sub('^data:image/.+;base64,', '', data)
#         # Create a new Signature instance
#         signature = Signature(image=image_data)
#         procesarfirma()
#         signature.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False}, status=400)


import base64
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from .models import Signature  # Adjust according to your model's location


@csrf_exempt  # Use this if you're not using CSRF tokens or for testing; otherwise, use CSRF protection
def save_signature(request, id_PDF):
    if request.method == "POST":
        image_data = request.POST.get("image")
        if image_data:
            # Remove the header (data:image/png;base64,)
            format, imgstr = image_data.split(";base64,")
            ext = format.split("/")[-1]  # 'png'
            img_data = ContentFile(base64.b64decode(imgstr), name="signature." + ext)

            # Save it to the model
            signature = Signature(image=img_data)
            signature.save()

            firma = Signature.objects.values("image").last()
            firma = firma["image"]

            # pdf=pdfEnviadosGerente.objects.values("documento_pdf").first()

            # pdf=pdfEnviadosGerente.objects.values("documento_pdf").last()

            ## Gerente general debe firmar el documento  orden de compra
            if user_is_in_group(request.user, "GERENCIA GENERAL"):
                try:

                    user_id = request.user.id

                    pdf = (
                        pdf2EnviadoGGeneral.objects.filter(id=id_PDF)
                        .values("documento_pdf")
                        .last()
                    )

                    id_gerente_instance = UsuariosTrime.objects.get(id=user_id)

                    id_pdf_instance = pdf2EnviadoGGeneral.objects.get(id=id_PDF)

                    print(pdf)

                    pdf = pdf["documento_pdf"]

                    print(pdf, firma)

                    modified_pdf_path = procesarfirma(pdf, firma, 450, 500)

                    with open(modified_pdf_path, "rb") as f:
                        modified_pdf_instance = pdf2EnviadoGGeneral.objects.get(
                            id=id_PDF
                        )

                        modified_pdf_instance.ESTATUS_DOCUMENTO = "Firmado por GG"
                        modified_pdf_instance.documento_pdf.save(
                            os.path.basename(modified_pdf_path), File(f)
                        )

                        modified_pdf_instance.save()

                    # pdf_enviado_almacen = pdf2EnviadoGGeneral.objects.create(
                    #    usuario=id_gerente_instance,
                    #   documento_pdf=id_pdf_instance,
                    #   )

                except Exception as e:
                    print(f"An error occurred: {e}")

            ## Gerente debe firmar el documento  requisicion
            elif user_is_in_group(request.user, "GERENTE"):
                try:

                    user_id = request.user.id

                    pdf = (
                        pdfEnviadosGerente.objects.filter(id=id_PDF)
                        .values("documento_pdf")
                        .last()
                    )

                    id_gerente_instance = UsuariosTrime.objects.get(id=user_id)

                    id_pdf_instance = pdfEnviadosGerente.objects.get(id=id_PDF)

                    print(pdf)

                    pdf = pdf["documento_pdf"]

                    print(pdf, firma)

                    modified_pdf_path = procesarfirma(pdf, firma, 100, 500)

                    # Step 12: Save the modified PDF to the database
                    with open(modified_pdf_path, "rb") as f:
                        modified_pdf_instance = pdfEnviadosGerente.objects.get(
                            id=id_PDF
                        )

                        modified_pdf_instance.ESTATUS_DOCUMENTO = "FIRMADO"
                        modified_pdf_instance.documento_pdf.save(
                            os.path.basename(modified_pdf_path), File(f)
                        )

                        modified_pdf_instance.save()

                    pdf_enviado_almacen = pdfEnviadosAlmacen.objects.create(
                        usuario=id_gerente_instance,
                        documento_pdf=id_pdf_instance,
                    )

                except Exception as e:
                    print(f"An error occurred: {e}")

            ## Gerente de alamcen debe firmar el documento  solicitud de orden de compra
            elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE ALMACEN"):
                try:

                    user_id = request.user.id

                    pdf = (
                        solicitudOrdendeCompras.objects.filter(id=id_PDF)
                        .values("documento_pdf")
                        .last()
                    )

                    pdf_instance = (
                        solicitudOrdendeCompras.objects.filter(id=id_PDF)
                        .values("requisicionCancelada")
                        .last()
                    )

                    pdf_instance = pdf_instance["requisicionCancelada"]
                    print(pdf_instance)

                    id_gerente_instance = UsuariosTrime.objects.get(id=user_id)

                    id_pdf_instance = pdfEnviadosAlmacen.objects.get(id=pdf_instance)

                    print(id_pdf_instance)

                    # id_pdf_instance=

                    print(pdf)

                    pdf = pdf["documento_pdf"]

                    print(pdf, firma)

                    modified_pdf_path = procesarfirma(pdf, firma, 100, 500)

                    # Step 12: Save the modified PDF to the database
                    with open(modified_pdf_path, "rb") as f:
                        modified_pdf_instance = solicitudOrdendeCompras.objects.get(
                            id=id_PDF
                        )

                        modified_pdf_instance.ESTATUS_DOCUMENTO = "FIRMADO"
                        modified_pdf_instance.documento_pdf.save(
                            os.path.basename(modified_pdf_path), File(f)
                        )

                        modified_pdf_instance.save()

                except Exception as e:
                    print(f"An error occurred: {e}")

                # pdf_enviado_almacen = solicitudOrdendeCompras.objects.create(
                #     usuario=id_gerente_instance,
                #         requisicionCancelada=id_pdf_instance,
                #         )

            ## Gerente de alamcen debe firmar el documento  solicitud de orden de compra
            elif user_is_in_group(request.user, "GERENTE DE DEPARTAMENTO DE COMPRAS"):

                try:

                    user_id = request.user.id

                    pdf = (
                        pdf2EnviadoGGeneral.objects.filter(id=id_PDF)
                        .values("documento_pdf")
                        .last()
                    )

                    id_gerente_instance = UsuariosTrime.objects.get(id=user_id)

                    id_pdf_instance = pdf2EnviadoGGeneral.objects.get(id=id_PDF)

                    print(pdf)

                    pdf = pdf["documento_pdf"]

                    print(pdf, firma)

                    modified_pdf_path = procesarfirma(pdf, firma, 100, 500)

                    with open(modified_pdf_path, "rb") as f:
                        modified_pdf_instance = pdf2EnviadoGGeneral.objects.get(
                            id=id_PDF
                        )

                        modified_pdf_instance.ESTATUS_DOCUMENTO = "Firmado por Compras"
                        modified_pdf_instance.documento_pdf.save(
                            os.path.basename(modified_pdf_path), File(f)
                        )

                        modified_pdf_instance.save()

                    # pdf_enviado_almacen = pdf2EnviadoGGeneral.objects.create(
                    #    usuario=id_gerente_instance,
                    #   documento_pdf=id_pdf_instance,
                    #   )

                except Exception as e:
                    print(f"An error occurred: {e}")

            else:
                print("NO SE GUARDO EL PDF EN BASE DE DATOS")

            # pdfEnviadosGerente.objects.filter(id=id_PDF).update(
            #     ESTATUS_DOCUMENTO="FIRMADO",
            #     documento_pdf = modified_pdf_path,
            #     )

            # finally:
            #     # Ensure the PDF is closed if it was opened
            #     try:
            #         pdf_document.close()
            #     except:
            #         pass

            # modified_pdf_path ="media/modified_example.pdf"
            # pdf_document.save(modified_pdf_path)  # Save as a new file or overwrite

            # # Step 12: Save the modified PDF to the database
            # with open(modified_pdf_path, 'rb') as f:
            #     modified_pdf_instance = Signature()
            #     modified_pdf_instance.pdf_file_firmado.save(os.path.basename(modified_pdf_path), File(f))
            #     modified_pdf_instance.save()

            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "No image data provided."})
    return JsonResponse({"success": False, "error": "Invalid request method."})
