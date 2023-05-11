# from argparse import _AttributeHolder
from django.db import models
from django.conf import settings
import os.path
# from forms import OpsPageForm 

class OpsPageInfo(models.Model):
        campaign_name = models.CharField(max_length=100, unique=True, blank=True)
        campaign_pic = models.ImageField(upload_to="static/opspage_pics")
        description_header = models.CharField(max_length=100, blank=True)
        campaign_description = models.CharField(max_length=600, blank=True)
        goal = models.CharField(max_length=100, blank=True)
        perk_header1 = models.CharField(max_length=100, blank=True)
        perk_description1 = models.CharField(max_length=600, blank=True)


        def __str__(self) -> str:
                return self.campaign_name



class Contact(models.Model):
        First_name = models.CharField(max_length=20)
        Last_name = models.CharField(max_length=20)
        username = models.CharField( max_length=30)
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50)
        zip = models.IntegerField()
        email = models.EmailField()
        desc= models.CharField(max_length=500)
        def __str__(self) -> str:
                return self.username
        

class Image(models.Model):
        photo = models.ImageField(upload_to="myimage")
        date = models.DateTimeField(auto_now_add=True)
        
        