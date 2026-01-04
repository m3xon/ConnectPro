from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class UserMd(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ('client', 'Client (Looking for developers)'),
        ('developer', 'Developer (Looking for projects)'),
    ]

    full_name = models.CharField(max_length= 100, blank= False)
    email = models.EmailField(unique= True, blank= False)
    password = models.CharField(blank= False)
    user_type = models.CharField(max_length=10, choices=ROLE_CHOICES, default='developer')
    # major = models.CharField(max_length=200, default="---")
    # address = models.CharField(max_length= 200, default= "---")
    joined_date = models.DateField(default= datetime.date.today)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'user_type']

    def __str__(self):
        return self.email