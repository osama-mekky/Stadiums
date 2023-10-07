from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

import datetime 
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pitche(models.Model):
    Name = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    location = models.CharField(max_length=500)
    name_of_supervisor = models.CharField(max_length=50)
    phone_of_supervisor = models.CharField(max_length=11)
    manager = models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.Name
    


timing = [
    ("one Hour",'one hour'),
    ("Tow Hour",'Tow hour'),
    ("Three Hour",'Three hour'),

]

period =[
    ('AM','AM'),
    ('PM','PM'),
]

class OpeningHours(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pitche = models.ForeignKey(Pitche,on_delete=models.DO_NOTHING)
    from_hour = models.DateTimeField(default=datetime.datetime.now())
    to_hour = models.DateTimeField(default=datetime.datetime.now())
    timing = models.CharField(max_length=50,choices=timing)


    def __str__(self):
        return f"{self.pitche}-{self.from_hour.time()} to {self.to_hour.time()}"
    class Meta :
        ordering =['-from_hour']
  
    def clean(self):
        if self.from_hour == self.to_hour:
            raise ValidationError('Wrong Time')
           

      
                    
        if (
            OpeningHours.objects.exclude(pk=self.pk)
            .filter(
                #made_on=self.made_on,
                #period=self.period,
                pitche_id=self.pitche_id,
                to_hour__gt=self.from_hour,
                from_hour__lt=self.to_hour,
            )
            .exists()
        ):
            raise ValidationError(
                f'The booked time ({self.from_hour} to {self.to_hour}) is occupied.'
            )
        return super().clean()




 # if OpeningHours.objects.filter(to_hour = self.to_hour).exists():
        #     raise ValidationError("Wrong")
       
        # if self.to_hour >datetime.time(0,00) and (self.from_hour == datetime.time(23,00) or self.from_hour==datetime.time(22,00)):
        #         if OpeningHours.objects.exclude(pk=self.pk).filter(made_on=self.made_on,pitche_id=self.pitche_id,to_hour =self.to_hour,from_hour=self.from_hour).exists():
        #                 raise ValidationError("Can Not")