import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class UnicodeUserphonelValidator(validators.RegexValidator):
    regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
    message = _(
            "Please enter a valid phone number (e.., +1234567890). This value should follow the international phone number format."
    )
    flags = 0
    
@deconstructible    
class OnlyNumberUserValidator(validators.RegexValidator):
    regex = r"^\d+$"
    message = _(
        "Enter a valid phone number. This value may contain only numbers."
    )
    flags = 0