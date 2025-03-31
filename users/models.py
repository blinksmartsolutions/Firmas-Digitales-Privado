

# Create your models here.

from datetime import date
from django.db import models
from django.core.validators import RegexValidator

from .choices import GENERO

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class UsuariosTrime(AbstractBaseUser, PermissionsMixin):
    #email = models.EmailField(_("email address"), unique=True)
    email =models.EmailField(verbose_name= "Correo", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    Nombre_Usuario = models.CharField(max_length = 60 , verbose_name="Nombre")
    Apellido_Usuario = models.CharField(max_length = 60, verbose_name="Apellido")
    Cedula_Usuario = models.CharField(max_length=18, verbose_name="CEDULA",unique=True)
    
    Departamento_Usuario = models.CharField(max_length=60, verbose_name="Departamento_Usuario",null=True )
    

    Edad_Usuario_new = models.DateField(auto_now_add=False, verbose_name='Fecha de Nacimiento', null=True )
    #Edad_Usuario = models.IntegerField(default=1, validators=[ MaxValueValidator(90), MinValueValidator(18)], verbose_name="Edad")
    #Fecha_nacimiento = models.CharField(max_length = 60, verbose_name='Fecha de Nacimiento')

    #mail_Usuario = models.EmailField(verbose_name= "Correo")
    Genero =  models.CharField(choices=GENERO, max_length=60, verbose_name="Género", default="MASCULINO")
    telefono_Usuario =models.CharField(verbose_name="Teléfono", max_length=18,validators=[RegexValidator('^\d{1,10}$')])

    fecha_creacion = models.DateField("Fecha de Creacion", auto_now= False, auto_now_add= True)
    fecha_modificacion = models.DateField("Fecha de Modificacion", auto_now= True, auto_now_add= False )
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios '

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def Edad_user(self):
        if self.Edad_Usuario_new:
            return (date.today() - self.Edad_Usuario_new.year)// 365
        return None


