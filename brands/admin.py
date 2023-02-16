from django.contrib import admin
from .models import Project , Project_Approval
# Register your models here.



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','project_brand','project_name','detail_about_project','total_cost','project_file')


@admin.register(Project_Approval)
class Project_ApprovalAdmin(admin.ModelAdmin):
    list_display = ('project','creator','creator_note')
