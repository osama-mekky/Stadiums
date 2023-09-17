from django.db import models

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pitche(models.Model):
    Name = models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    location = models.CharField(max_length=500)
    name_of_supervisor = models.CharField(max_length=50)
    phone_of_supervisor = models.CharField(max_length=11)
    manager = models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.Name

