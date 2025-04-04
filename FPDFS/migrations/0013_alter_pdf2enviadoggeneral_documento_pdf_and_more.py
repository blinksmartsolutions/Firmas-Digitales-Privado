# Generated by Django 4.2 on 2024-11-25 04:17

import FPDFS.models
import FPDFS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FPDFS", "0012_alter_pdfenviadosalmacen_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdf2enviadoggeneral",
            name="documento_pdf",
            field=models.FileField(
                upload_to=FPDFS.models.change_name,
                validators=[
                    FPDFS.validators.validate_file_extension,
                    FPDFS.validators.file_size,
                ],
                verbose_name="Orden de Compras",
            ),
        ),
        migrations.AlterField(
            model_name="pdf2enviadoggeneral",
            name="nombre_documento",
            field=models.CharField(
                max_length=22, null=True, verbose_name="Nombre del documento"
            ),
        ),
        migrations.AlterField(
            model_name="pdfenviadosgerente",
            name="documento_pdf",
            field=models.FileField(
                upload_to=FPDFS.models.change_name,
                validators=[
                    FPDFS.validators.validate_file_extension,
                    FPDFS.validators.file_size,
                ],
                verbose_name="Requisición",
            ),
        ),
        migrations.AlterField(
            model_name="solicitudordendecompras",
            name="documento_pdf",
            field=models.FileField(
                upload_to=FPDFS.models.change_name,
                validators=[
                    FPDFS.validators.validate_file_extension,
                    FPDFS.validators.file_size,
                ],
                verbose_name="Solicitud de Orden de Compras",
            ),
        ),
    ]
