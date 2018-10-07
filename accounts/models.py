from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .manager import AgentUserManager


class User(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(_('Овог'), max_length=15)
    first_name = models.CharField(_('Нэр'), max_length=15)
    email = models.EmailField(_('Имэйл хаяг'))
    phone_regex = RegexValidator(
        regex=r"(9[0-9])[0-9]{6}|(8[0-9])[0-9]{6}|(7[0-9])[0-9]{6}$", message="Зөв дугаар оруулна уу.")
    phone = models.CharField(
        validators=[phone_regex], max_length=8, unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    address = models.TextField(_('Хаяг'))

    USERNAME_FIELD = 'phone'
    objects = AgentUserManager()

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name
