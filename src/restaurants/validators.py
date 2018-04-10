from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError(_("We do not accept edu emails"))

CATEGORIES = ['Mexican', 'Fast Food', 'Gastronomic']

def validate_category(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		#raise ValidationError(_(f"{value} not a category valid"))
		raise ValidationError(
		    _('%(value)s not a category valid'),
		    code='invalid',
		    params={'value': value},
		)
		# raise ValidationError(_('Invalid value: %s') % value)