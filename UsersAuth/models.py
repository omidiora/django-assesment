from django.db import models

# Create your models here.
from django.db import models


from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, username,first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, password, first_name, last_name,):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email =             models.EmailField(verbose_name='email', max_length=60, unique=True)
    username =          models.CharField(max_length=30, unique=True)
    first_name =        models.CharField(verbose_name='first_name', max_length=30)
    last_name =         models.CharField(verbose_name='last_name', max_length=30)
    phone =            models.CharField(verbose_name='Phone', max_length=30  ,blank=True, null=True)
    Avatar =            models.FileField(upload_to='image' ,blank=True, null=True)

    USERNAME_FIELD = 'email' 
#this field means that when you try to sign in the username field will be the email 
#change it to whatever you want django to see as the username when authenticating the user
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    objects = MyUserManager()

    def __str__(self):
        return self.first_name + ' - ' + self.email

  