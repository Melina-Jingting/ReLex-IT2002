from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.



class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, groups, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not groups:
            raise ValueError("Users must have group")
        
        user = self.model(
                email       = self.normalize_email(email),
                groups  = groups
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, groups, password=None):
        user = self.create_user(
            email       = self.normalize_email(email),
            password    = password,
            groups      = groups
        )

        user.is_admin       = True
        user.is_staff       = True
        user.is_superuser   = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    email                   = models.EmailField(verbose_name='email',max_length=256,primary_key=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    groups                  = models.CharField(max_length=64)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    class Meta:
        db_table = 'auth_user'

