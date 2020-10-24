from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_coordinates(value):
    if len(value.split()) != 2:
        raise ValidationError(
            _('%(value)s is not an coordinates!'),
            params={'value': value},
        )