from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.pitches,name='pitches'),
    path('<int:id>',views.pitche_page,name='pitche'),

]