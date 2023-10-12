from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#signin page

class CustomerSignUp(models.Model):
    username = models.OneToOneField(User, unique=True, on_delete =models.CASCADE, related_name= 'customer')
    first_name = models.CharField(max_length= 250, blank=False)
    last_name = models.CharField(max_length =250, blank= False)
    email = models.EmailField(max_length= 100, blank =False)
    address =models.CharField(max_length=250, default='Soroti,Uganda', blank= True, null= True)
    profile_picture =models.ImageField(upload_to='profile_pic')
    designation = models.CharField(max_length=250, blank= False)
    phone =models.TextField(max_length=250, blank=True, default='0773323264')
    information= models.TextField(blank=True, null=True)


    def __str__(self):
        return self.username
    







