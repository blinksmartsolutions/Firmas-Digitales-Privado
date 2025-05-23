from django import forms


from .models import pdfEnviadosGerente

from .models import pdf2EnviadoGGeneral
from .models import solicitudOrdendeCompras


from django.core.validators import RegexValidator


class documentomixin(forms.ModelForm):
    nombre_documento = forms.CharField(
        required=True,
        label="Nombre del documento",
        min_length=6,
        validators=[
            RegexValidator(
                regex=r"^[\w.@ +-]+$",
                message=("Carácter no valido. solo se permite caracteres de A-Z"),
            )
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Agregue un Nombre del documento"}
        ),
    )

    N_documento = forms.CharField(
        required=True,
        label="Número del documento",
        min_length=5,
        validators=[
            RegexValidator(
                regex=r"^[\w.@ +-]+$",
                message=("Carácter no valido. solo se permite caracteres de A-Z"),
            )
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Agregue un número del documento"}
        ),
    )

    descripcion_documento = (
        forms.CharField(
            required=False,
            label="Descripción del documento",
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Agregue una descripción del documento",
                    "rows": 3,
                    "cols": 20,
                }
            ),
        ),
    )

    documento_pdf = forms.FileField(
        widget=forms.FileInput(attrs={"accept": "application/pdf", type: "file"}),
        # label='Nueva Requisición',
        required=False,
        validators=[
            RegexValidator(
                regex=r"^[\w,\s-]+\.[pdf]{3}$",
                message="solo se aceptan Pdf.",
                code="invalid_url",
            )
        ],
        help_text="Debes colocar solo archivos en formato pdf.",
    )

    class Meta:
        abstract = True


class cargarpdfUsuarioGeneralform(documentomixin):
    """Formulario para cargar el PDF del usuario basico y mandarlo al Gerente   Requisiciones"""

    title = "Cargar Requisición"  # Custom title

    class Meta:
        model = pdfEnviadosGerente
        fields = [
            "nombre_documento",
            "N_documento",
            "descripcion_documento",
            "documento_pdf",
        ]


class cambiarEStatuspdfUsuarioGeneralform(forms.ModelForm):
    """Formulario para cargar el PDF del usuario basico y mandarlo al Gerente   Requisiciones"""

    title = "Modificar Estatus"  # Custom title
    title2 = "Por favor comentar una descripción del motivo de la cancelación"  # Custom title

    class Meta:
        model = pdfEnviadosGerente
        fields = ["descripcion_documento"]


class cargarpdfsolicitudordencomprasform(documentomixin):
    """Formulario para cargar el PDF del usuario basico y mandarlo al Gerente   Solicitudes de orden de compras"""

    title = "Cargar Solicitud de Orden de Compras"  # Custom title

    class Meta:
        model = solicitudOrdendeCompras
        fields = [
            "nombre_documento",
            "N_documento",
            "descripcion_documento",
            "documento_pdf",
        ]


class cambiarEStatuspdfolicitudordencomprasform(forms.ModelForm):
    """Formulario para cargar el PDF del usuario basico y mandarlo al Gerente   Requisiciones"""

    title = "Modificar Estatus"  # Custom title
    title2 = "Por favor comentar una descripción del motivo de la cancelación"  # Custom title

    class Meta:
        model = solicitudOrdendeCompras
        fields = ["descripcion_documento"]


class cargarpdfOrdendeCompraform(documentomixin):
    """Formulario para cargar el PDF del usuario basico y mandarlo al Gerente  orden de compras"""

    title = "Cargar Orden de Compras"  # Custom title

    class Meta:
        model = pdf2EnviadoGGeneral
        fields = [
            "nombre_documento",
            "N_documento",
            "descripcion_documento",
            "documento_pdf",
        ]


class cambiarEStatuspdfordencomprasform(forms.ModelForm):
    """Formulario para cargar el PDF del usuario basico y mandarlo alorden de compras"""

    title = "Modificar Estatus Orden de Compras"  # Custom title
    title2 = "Por favor comentar una descripción del motivo de la cancelación"  # Custom title

    class Meta:
        model = pdf2EnviadoGGeneral
        fields = ["descripcion_documento"]
