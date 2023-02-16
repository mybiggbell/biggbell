from django.urls import path
from .views import creator_dashboard  , apply_project , creator_profile , cretor_project_all 
 

urlpatterns = [
    path('creator-dashboard/', creator_dashboard,name='creator_dashboard'),  
    path('apply-project/<int:id>/', apply_project,name='apply_project'),  
    path('creator-profile/', creator_profile,name='creator_profile'),  
    path('cretor-project-all/', cretor_project_all,name='cretor_project_all'),   
]