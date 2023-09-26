from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.utils import timezone


def pitches(request):
    context ={
        'pitche':Pitche.objects.all(),
    }
    return render(request,'pitches/pitches.html',context)






def pitche_page(request,id):

    if request.method == 'POST' and request.user.is_authenticated :
            instance = OpeningHours(pitche_id=id, user=request.user)
            add_date = RestaurantForm(request.POST, request.FILES, instance=instance)
            if add_date.is_valid():
                add_date.save()
                messages.success(request, "Booking Successful")
            else:
                messages.error(request, 'this time is booked before') 
    
    context ={
        'pit':get_object_or_404(Pitche,id=id),
        'form':RestaurantForm(),
    }
    return render(request,'pitches/pitche.html',context)











# add_date = RestaurantForm(request.POST)
#             pit_id = Pitche.objects.get(id =id )
#             from_hour=add_date['from_hour'].value()
#             to_hour=add_date['to_hour'].value()
#             made_on=add_date['made_on'].value()
#             period = add_date['period'].value()
#             unieck = request.POST['pit']

#             in_range = (from_hour,to_hour)
#             #filter = OpeningHours.objects.filter(made_on=made_on,period = period).filter(Q(from_hour__range=in_range) | Q(to_hour__range=in_range)).exists()
#             x= Pitche.objects.filter(id=unieck)
#             if OpeningHours.objects.filter(made_on=made_on,period = period).filter(Q(from_hour__range=in_range) | Q(to_hour__range=in_range)).exists():
#                 messages.error(request,"Not Allowed")
#             else:     
#                 #add_date = RestaurantForm(request.POST)
#                 if add_date.is_valid():
#                     info =add_date.save(commit=False)
#                     login_user = User.objects.get(username = request.user.username)
#                     info.user = login_user
#                     info.pitche = pit_id
#                     info.save()
#                     messages.success(request,"Booking Successful")
#                 else:
#                     messages.error(request,"this time is booked befor") 