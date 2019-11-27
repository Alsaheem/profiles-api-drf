from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('users must have an email address')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,password):
        user = self.create_user(email,first_name,last_name,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserProfileManager()
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    
    def get_short_name(self):
        return '{}.{}'.format(self.first_name[0],self.last_name[0])

    def __str__(self):
        return self.email

class ProfileFeed(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text