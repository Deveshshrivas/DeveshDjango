from django.db import models



# Create your models here.



import string
import random

class Otp:
    def __init__(self, length=6):
        self._length = length
        self._characters = string.ascii_letters + string.digits
    
    def generate(self):
        return ''.join(random.sample(self._characters, self._length))
my_otp = Otp() 


