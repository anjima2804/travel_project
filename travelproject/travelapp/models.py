from django.db import models
from pyexpat import model


# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()



class team(models.Model):
    name1=models.CharField(max_length=250)
    imgg=models.ImageField(upload_to='pic')
    des=models.TextField()

def __str__(self):
    return self.name()





