from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from users.models import  UsuariosTrime 

from .validators import validate_file_extension, validate_file_extension2
from .validators import file_size, file_size2


from datetime import date
from datetime import datetime
from django.utils import timezone
now = timezone.now()

import uuid  

# Create your models here.



class TimestampMixin(models.Model):
    fecha_creacion = models.DateField("Fecha de Creacion", auto_now= False, auto_now_add= True)
    fecha_modificacion = models.DateField("Fecha de Modificacion", auto_now= True, auto_now_add= False)

    class Meta:
        abstract = True



class AuditMixin(models.Model):
    pass


def change_name(instance, filename):
    random_string = uuid.uuid4().hex[:6]  # generate a 6-character random string
    filename =  f"{random_string}_{filename}"
    time= now.strftime("%Y/%m/%d")
    filename= "files/" +  filename  
    
    return filename 




ESTATUS = (
("ENVIADO", "ENVIADO"),
("FIRMADO", "FIRMADO"),
("RECHAZADO", "RECHAZADO"),
("Aceptado por Almacen", "Aceptado por Almacen"),
("Firmado por Compras", "Firmado por Compras"),
("Firmado por GG", "Firmado por GG"),
("Rechazado por Compras", "Rechazado por Compras"),	
("Rechazado por GG", "Rechazado por GG"),	
("Rechazado por Almacen", "Rechazado por Almacen"),	
("COTIZANDO", "COTIZANDO"),
("EN ESPERA", "EN ESPERA"),

("Rechazado por Gerente", "Rechazado por Gerente"),

("Generada ODC", "Generada ODC"),


    
)



###===================================== REQUISICIONES ===========================


class pdfEnviadosGerente(TimestampMixin):
    
    """ modelo donde se guarda el documento de REQUISICION  enviado por USUARIO 
    """ 
    
    
    nombre_documento = models.TextField(verbose_name="Nombre del documento", null=True)
    N_documento = models.CharField(
        max_length=5,
        verbose_name="Numero del documento", 
        null=True, 
    )
    descripcion_documento= models.TextField(blank=True, null=True, verbose_name="Descripción del documento" )
   
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    documento_pdf = models.FileField(upload_to=change_name, validators=[validate_file_extension, file_size],  verbose_name="Requisición")
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Requisiciones a los Gerentes'
        verbose_name_plural = 'PDFtoGerente'

    def __str__(self):
        return str(self.usuario) 
    
    
    def delete(self, using=None, keep_parents=False):
        self.documento_pdf.storage.delete(self.documento_pdf.name)

        super().delete()     



class pdfEnviadosAlmacen(TimestampMixin):
    
    """ modelo donde se guarda el documento de REQUISICION  enviado por GERENTE 
    """ 
   
   
   
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    documento_pdf = models.ForeignKey(pdfEnviadosGerente, on_delete = models.CASCADE)
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Requisiciones Departamento de Almacen'
        verbose_name_plural = 'PDFtoAlmacen'

    def __str__(self):
        return str(self.documento_pdf) 
    
    
class pdfEnviadosCompras(TimestampMixin):
    """ modelo donde se guarda el documento de REQUISICION  enviado por Almacen 
    """ 
   
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    documento_pdf = models.ForeignKey(pdfEnviadosAlmacen, on_delete = models.CASCADE)
    #documento_pdf = models.FileField(upload_to=change_name, validators=[validate_file_extension, file_size])
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Requisiciones Departamento de Compras'


    def __str__(self):
        return str(self.usuario)   +  "  "  + str(self.documento_pdf) 







###===================================== SOLICITUD DE ORDENES DE COMPRAS ===========================

class solicitudOrdendeCompras(TimestampMixin):
    """ modelo donde se guarda el documento de SOLICITUD DE ORDENES DE COMPRAS por los usuarios de departamento de ALMACEN

    """ 
    
    
    nombre_documento =  models.CharField(max_length=22, verbose_name="Nombre del documento",  null=True)
    N_documento =  models.CharField(max_length=22, verbose_name="Numero del documento", null=True) 
    descripcion_documento= models.CharField(max_length=460,blank=True, null=True, verbose_name="Descripción del documento" )
    
    
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    requisicionCancelada = models.ForeignKey(pdfEnviadosAlmacen, on_delete = models.CASCADE) 

    documento_pdf = models.FileField(upload_to=change_name, validators=[validate_file_extension, file_size],  verbose_name="Solicitud de Orden de Compras")
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Solicitud de orden de compras'
        verbose_name_plural = 'Solicitud de orden de compras'

    def __str__(self):
        return str(self.usuario)  

    def delete(self, using=None, keep_parents=False):
        self.documento_pdf.storage.delete(self.documento_pdf.name)

        super().delete()  



###===================================== COTIZACIONES ===========================

class cotizaciondeCompras(TimestampMixin):
    """ modelo donde se guarda el documento de cotizaciones por los usuarios del departamento de compras
    """ 
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    solcitudOrdendeCompras = models.ForeignKey(solicitudOrdendeCompras, on_delete = models.CASCADE)
    
    nombre_documento=models.CharField(max_length=60,)
    documento_pdf = models.FileField(upload_to=change_name, validators=[validate_file_extension, file_size])
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    def __str__(self):
        return str(self.usuario)  
    
    
   
   
   
   


   
### ==============================  ORDENES DE COMPRAS ============================    
class pdf2EnviadoGGeneral(TimestampMixin):
    """ modelo donde se guarda el documento de ordenes de compras
    """    
    
    nombre_documento =  models.CharField(max_length=22, verbose_name="Nombre del documento",  null=True)
    N_documento =  models.CharField(max_length=22, verbose_name="Numero del documento", null=True) 
    descripcion_documento= models.CharField(max_length=460,blank=True, null=True, verbose_name="Descripción del documento" )
    
    usuario = models.ForeignKey(UsuariosTrime, on_delete = models.CASCADE)
    cotizacionAcecptada = models.ForeignKey(solicitudOrdendeCompras, on_delete = models.CASCADE)
    documento_pdf = models.FileField(upload_to=change_name, validators=[validate_file_extension, file_size], verbose_name="Orden de Compras")
    ESTATUS_DOCUMENTO = models.CharField(choices=ESTATUS, max_length=22, verbose_name="ESTADO DEL DOCUMENTO", default="ENVIADO")
    

    class Meta:
        verbose_name = 'Orden de Compra'
        verbose_name_plural = 'Ordenes de Compras'

    def __str__(self):
        return str(self.usuario)  
    
    def delete(self, using=None, keep_parents=False):
        self.documento_pdf.storage.delete(self.documento_pdf.name)

        super().delete()  
    






class Signature(TimestampMixin):
    image = models.ImageField(upload_to='firmas/')  # Store the Base64 string
    pdf_file_firmado = models.FileField(upload_to='pdfs/', blank=True)  # For storing the PDF file
    
    
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)

        super().delete()  