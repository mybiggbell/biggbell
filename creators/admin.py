from django.contrib import admin
from creators.models import CreatorInbox
# Register your models here.

@admin.register(CreatorInbox)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','creator','brand','email','file','description','isseen')
