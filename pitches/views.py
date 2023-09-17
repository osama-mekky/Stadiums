from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404


def pitches(request):
    context ={
        'pitche':Pitche.objects.all(),
    }
    return render(request,'pitches/pitches.html',context)

def pitche(request,id):
    context ={
        'pit':get_object_or_404(Pitche,id=id)
    }
    return render(request,'pitches/pitche.html',context)
