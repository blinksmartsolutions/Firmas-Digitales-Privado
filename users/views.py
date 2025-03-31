from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def login(request):
    return render(request, "login/login.html")

# funcion de validacion de usuario
def register(request):
    pass
    # if request.method == "POST":
    #     form = UserRegisterForm(request.POST)
    #     usuarios = UserRegisterForm()

    #     if form.is_valid():


    #         email = form.cleaned_data.get('email')
    #         # if User.objects.filter(email=email).exists():
    #         #     messages.warning(request, 'Este Email ya existe')
    #         #     return redirect('register')
    #         form.save()
    #         username = form.cleaned_data.get('Nombre_Usuario')
    #         # email = form.cleaned_data.get('email') 
    #         html_message = render_to_string("correos/bienvenida.html", {"username":username})
    #         plain_message = strip_tags(html_message) 
    #         mail.send_mail('Regionales WRO México 2024',plain_message,'wromexico@fundesteam.org',[email],html_message=html_message)
    #         messages.success(request, f'Hola {username}, tu cuenta fue creada exitosamente')
    #         return redirect('login')
    # else:
    #     form = UserRegisterForm()

    # return render(request, 'paginas/register.html', {
    #     'form': form,
    #     })