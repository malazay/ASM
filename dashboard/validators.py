import os
from django.core.exceptions import ValidationError


def validate_path(value):
    if os.path.isfile(value) is False:
        raise ValidationError('The file is not present in %s' % value)
