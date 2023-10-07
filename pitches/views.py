from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q

def pitches(request):
    q=''

    if request.GET.get('q') != None :
         q= request.GET.get('q')
    else :
         ''     
    pitche = Pitche.objects.filter(Q(city__name__icontains=q)|Q(Name__icontains = q))
    pitche_count=pitche.count()

    context ={
        'pitche':pitche,
        'citys' :City.objects.all(),
        'pitche_count':pitche_count,   

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



def delateBooking(request,id):
     booking = OpeningHours.objects.get(id=id)
     if booking.user.id == request.user.id:
        booking.delete()
    #  if request.method == 'POST':
    #     booking.delete()
     return redirect('profile')







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