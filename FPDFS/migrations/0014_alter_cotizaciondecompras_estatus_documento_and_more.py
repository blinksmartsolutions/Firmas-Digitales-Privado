# Generated by Django 5.1.7 on 2025-03-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FPDFS", "0013_alter_pdf2enviadoggeneral_documento_pdf_and_more"),
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
                    ("Generada ODC", "Generada ODC"),
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
                    ("Generada ODC", "Generada ODC"),
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
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
                    ("Generada ODC", "Generada ODC"),
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
                    ("Generada ODC", "Generada ODC"),
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
                    ("Generada ODC", "Generada ODC"),
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
                    ("Generada ODC", "Generada ODC"),
                ],
                default="ENVIADO",
                max_length=22,
                verbose_name="ESTADO DEL DOCUMENTO",
            ),
        ),
    ]
