# Generated by Django 4.2 on 2024-11-24 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("FPDFS", "0009_alter_cotizaciondecompras_estatus_documento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cotizaciondecompras",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
        migrations.AlterField(
            model_name="pdf2enviadoggeneral",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
        migrations.AlterField(
            model_name="pdf2enviadoggeneral",
            name="cotizacionAcecptada",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="FPDFS.solicitudordendecompras",
            ),
        ),
        migrations.AlterField(
            model_name="pdfenviadosalmacen",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
        migrations.AlterField(
            model_name="pdfenviadoscompras",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
        migrations.AlterField(
            model_name="pdfenviadosgerente",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
        migrations.AlterField(
            model_name="solicitudordendecompras",
            name="ESTATUS_DOCUMENTO",
            field=models.CharField(
                choices=[
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
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
    ]
