import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf", ".PDF"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Tipo de archivo no aceptado solo .pdf ")


def validate_file_extension2(value):

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".mp4", ".MP4"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Tipo de archivo no aceptado solo .mp4")


def file_size(value):  # add this to some file where you can import it from
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            "El archivo excede el limite permitido. Debe ser menor de 5MB"
        )


def file_size2(value):  # add this to some file where you can import it from
    limit = 150 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            "El archivo excede el limite permitido. Debe ser menor de 150MB"
        )
