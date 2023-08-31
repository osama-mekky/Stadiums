from django.db import models

# Create your models here.


class Pitche(models.Model):
    Name = models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    location = models.CharField(max_length=500)
    

    def __str__(self):
        return self.Name

