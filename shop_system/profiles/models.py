import datetime
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):        
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),)        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password=password,)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user        

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    role = models.CharField(max_length=10,default='')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):            
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"    
        return True
    @property
    def get_role(self):
        "Is the user ?"
        return self.role

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active   


    objects = UserManager()

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(max_length=25 ,default='pending')
    date = models.DateField( default=datetime.date.today)

class ProductInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.IntegerField()
