import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, country, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)  # Por defecto, is_staff es True
        extra_fields.setdefault("is_superuser", False)  # No será superusuario

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, country, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, first_name, last_name, country, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    usertype_default = [
        ('AD', 'admin'),
        ('ST', 'standard'),
    ]
    id = models.AutoField(primary_key=True)
    id_perfil = models.CharField(max_length=32, unique=False, editable=False, default=uuid.uuid4().hex)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True) 
    usertype = models.CharField(
        max_length=3,
        choices=usertype_default,
        blank=False,
        null=False,
        default="ST",
        help_text="Type of user, such as admin or standard"
    )
    objects = CustomUserManager()

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country']

    def __str__(self):
        return self.email
