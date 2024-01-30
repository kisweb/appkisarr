from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user_(self, name, username, role, email, password, **extra_fields):
        if not email:
            raise ValueError('You did not provide an valid e-amil address')
    
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, name=None, username=None, email=None, role=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user_(name, username, email, password, **extra_fields)
    

    def create_superuser(self, name=None, username=None, email=None, role=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user_(name, email, password, **extra_fields)

class CustomUser(AbstractUser):
    class RoleDef(models.TextChoices):
        DIRECTEUR = 'Directeur', 'Directeur'
        GESTIONNAIRE = 'Gestionnaire', 'Gestionnaire'
        CONSEILLER = 'Conseiller', 'Conseiller'
        USER = 'Utilisateur', 'Utilisateur'
        
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="p_img", blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    role = models.CharField(max_length=50, choices=RoleDef.choices, blank=True, null=True, default='Utilisateur')
    bio = models.TextField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    
    def __str__(self):
        return self.email
    
class Contact(models.Model):
    email = models.EmailField() 
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, null=True, blank=True)
    message = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {self.email}"