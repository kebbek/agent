from django.contrib.auth.models import BaseUserManager


class AgentUserManager(BaseUserManager):

    def _create_user(self, phone, password, **extra):
        if not phone:
            raise ValueError('Утасны дугаар олдсонгүй.')

        phone = phone
        user = self.model(phone=phone, **extra)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, password, **extra_fields)
