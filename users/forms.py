from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator
from .models import UsuariosTrime


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AdminPasswordChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UsuariosTrime
        fields = ("email", "Cedula_Usuario")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UsuariosTrime
        fields = ("email",)


class AdminPasswordChangeForm(AdminPasswordChangeForm):
    class Meta:
        model = UsuariosTrime
        fields = (
            "password",
            "new_password1",
            "new_password2",
        )


class UserRegisterForm(UserCreationForm):
    # username= forms.CharField(required=True, label="Nombre de Usuario", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Agregue un Nombre de Usuario'}))
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.TextInput(attrs={"placeholder": "Agregue su Correo Electrónico"}),
    )
    Nombre_Usuario = forms.CharField(
        min_length=6,
        required=True,
        label="Nombre(s)",
        max_length=40,
        widget=forms.TextInput(attrs={"placeholder": "Agregue su nombre completo"}),
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*$",
                message=("Carácter no valido. solo se permite caracteres de A-Z"),
            )
        ],
    )
    Apellido_Usuario = forms.CharField(
        min_length=6,
        required=True,
        label="Apellido(s)",
        max_length=40,
        widget=forms.TextInput(attrs={"placeholder": "Agregue su apellido completo"}),
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*\s{,1}[a-zA-Z_ÑñÁáÉéÍíÓóÚú]*$",
                message=("Carácter no valido. solo se permite caracteres de A-Z"),
            )
        ],
    )

    class Meta:
        # model = Users

        model = UsuariosTrime
        # fields = '__all__'

        fields = [
            "email",
            "Nombre_Usuario",
            "Apellido_Usuario",
            "Edad_Usuario_new",
            "Departamento_Usuario",
            "password1",
            "password2",
        ]
