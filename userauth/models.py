from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
import uuid
 

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,contact_number,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,last_name,contact_number,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




CHOICES_GENDER = [
    ("Male", _("Male")),
    ("Female", _("Female")),
    ("Other", _("Other"))
]

 
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
     
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email_verified = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    last_visit = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES_GENDER)
    country_name = models.CharField(max_length=30, blank=True, null=True, default='')
    

    is_creator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','contact_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


 

class Creator(models.Model):
     
    person = models.OneToOneField(
        MyUser, related_name="creators", on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='creator_profile', height_field=None, width_field=None, max_length=None)
    youtube_name =models.CharField(max_length=150,blank=True)
    instagram_name =models.CharField(max_length=150,blank=True)
    email_code = models.CharField(max_length=400)
    youtube_link =  models.URLField(max_length = 200)
    instagram_link =  models.URLField(max_length = 200)
    linkedin_link = models.URLField(max_length=200)
    type_of_youtube = models.CharField(max_length=250)
    youtube_subscriber = models.IntegerField(default=0, blank=True, null=True)
    instagram_followers = models.IntegerField(default=0, blank=True, null=True)
    low_Budget = models.IntegerField(default=0, blank=True, null=True)
    high_Budget = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.person)

class Brand(models.Model):
    person = models.OneToOneField(
        MyUser, related_name="brand", on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='brands_profile', height_field=None, width_field=None, max_length=None)
    company_name = models.CharField(max_length=150)
    company_profile_link = models.URLField(max_length=150)
    company_official_email = models.EmailField(max_length=250)

    def __str__(self):
        return "{}".format(self.person)
    
 