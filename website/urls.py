from django.urls import path
from .views import home , how_it_work


urlpatterns = [
     path('',home,name='home'),
     path('how-it-work/',how_it_work,name='how_it_work'),
]
