from django.urls import path
from .views import brand_dashboard , post_a_project , payment_page , creator_profile_see , project_list , accept , complete_done , creator_profile_for_brand , project_details , brands_profile , success
 

urlpatterns = [
    path('brand-dashboard/', brand_dashboard,name='brand_dashboard'),  
    path('post-a-project/', post_a_project,name='post_a_project'),  
    path('payment-page/',payment_page,name='payment_page'),
    # path('creator-profile/<int:id>/',creator_profile_see,name='creator_profile_see'),
    path('project-list/',project_list,name='project_list'),
    path('accept/<int:id>/',accept,name='accept'),
    path('complete-done/<int:id>/',complete_done,name='complete_done'),
    
    path('creator-profiles/<int:id>/', creator_profile_for_brand,name='creator_profile_for_brand'), 
    path('project-details/<int:id>/', project_details,name='project_details'), 
    path('brands-profile/', brands_profile,name='brands_profile'), 
    path('success/', success,name='success'), 
]