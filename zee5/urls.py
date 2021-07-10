from django.urls import path
from .views import *

urlpatterns = [
   path('', home, name="home"),
   path('zee5/', zee5 , name= "zee5")
]
