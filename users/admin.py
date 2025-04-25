from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from users.forms import AdminPasswordChangeForm
from users.forms import CustomUserCreationForm
from users.forms import CustomUserChangeForm

from users.models import UsuariosTrime
from import_export.admin import ImportExportModelAdmin

# admin.site.register(UsuariosTrime)


@admin.register(UsuariosTrime)
class UsuariosTrimeAdmin(ImportExportModelAdmin, UserAdmin):
    change_password_form = AdminPasswordChangeForm
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuariosTrime
    list_display = (
        "id",
        "email",
        "is_staff",
        "is_active",
        "Cedula_Usuario",
        "Edad_Usuario_new",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "Cedula_Usuario",
                    "Edad_Usuario_new",
                    "Departamento_Usuario",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "Cedula_Usuario",
                    "password1",
                    "password2",
                    "is_staff",
                    "Edad_Usuario_new",
                    "Departamento_Usuario",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
