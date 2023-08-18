from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyAccountManager(BaseUserManager):

    # Creating Normal User

    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError('User Must Have An Email.')

        if not username:
            raise ValueError('User Must Have An Username, Its Your Identity.')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,

        )
        user.is_active = True
        user.set_password(password)
        user.save(self._db)
        return user

    # Creating Super User.

    def create_superuser(self, first_name, last_name, email, username, password):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    # Add Your Fields

    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # Add A Created Manager

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def getEmail(self):
        return f'{self.email}'
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True