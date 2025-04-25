from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_view


urlpatterns = [
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="login/login.html"),
        name="login",
    ),
    path("register/", views.register, name="register"),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="paginas/logout.html"),
        name="logout",
    ),
    path(
        "reset_password/",
        auth_view.PasswordResetView.as_view(
            template_name="paginas/reset_password.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="paginas/reset_password_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="paginas/reset_password_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="paginas/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
]
