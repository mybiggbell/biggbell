from django.urls import path
from .views import login_user , brands_register , creator_register , next_register_cretor,next_register_brand , user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_user,name='login_user'),
    path('brand-register/', brands_register,name='brands_register'),
    path('creator-register/', creator_register,name='creator_register'),
    path('next-register-cretor/',next_register_cretor,name='next_register_cretor'),  
    path('next-register-brand/',next_register_brand,name='next_register_brand') ,
    path('user-logout/',user_logout,name='user_logout') ,
 
]