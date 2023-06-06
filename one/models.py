from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.


class Makeuser(BaseUserManager):
    def create_user(self,email,username,password,**exter_field):
        if not email:
            raise ValueError('User Should Have email')
        if not username:
            raise ValueError('User Should have username')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,username,password,**exter_field):
        user = self.create_user(
            username=username,
            email=email,
            password = password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user







class NewUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    bio = models.ImageField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_create = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['username',]
    USERNAME_FIELD = 'email'
    objects = Makeuser()





class Airport(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length=12)


    def __str__(self):
        return f'({self.code}) {self.city}'





class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.origin} {self.destination} {self.duration}'



class Passenger(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    flights = models.ManyToManyField(Flight,blank=True,null=True,related_name='passengers')


    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


    
