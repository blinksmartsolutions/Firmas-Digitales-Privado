

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from FPDFS.models import pdfEnviadosGerente
from FPDFS.models import pdfEnviadosAlmacen
from FPDFS.models import pdfEnviadosCompras

from FPDFS.models import pdf2EnviadoGGeneral

from FPDFS.models import solicitudOrdendeCompras




from FPDFS.models import Signature



# Crear una instancia personalizada de AdminSite
admin.site.site_header = 'Panel Administrativo de TRIME, C.A.'
admin.site.index_title = 'Panel de control de TRIME, C.A.'
admin.site.site_title = 'Administración de TRIME, C.A.'




class pdfEnviadosGerenteAdmin(admin.ModelAdmin):
    list_display = ( "id" , "usuario" , "documento_pdf", "ESTATUS_DOCUMENTO", )
    

    
    
admin.site.register(pdfEnviadosGerente,pdfEnviadosGerenteAdmin)


class pdfEnviadosAlmacenAdmin(admin.ModelAdmin):
    list_display = ( "id" , "usuario" , "documento_pdf", "ESTATUS_DOCUMENTO",)


 

admin.site.register(pdfEnviadosAlmacen,pdfEnviadosAlmacenAdmin)







admin.site.register(pdfEnviadosCompras)
admin.site.register(solicitudOrdendeCompras)





class pdf2EnviadoGGeneralAdmin(admin.ModelAdmin):
    list_display = ( "id" , "usuario" , "cotizacionAcecptada", "nombre_documento", "documento_pdf", "ESTATUS_DOCUMENTO" )


admin.site.register(pdf2EnviadoGGeneral,pdf2EnviadoGGeneralAdmin)



admin.site.register(Signature)









