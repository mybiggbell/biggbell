from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser , Creator ,Brand


class MyUserAdmin(BaseUserAdmin):
    list_display = ('email','first_name','last_name','contact_number','email_verified','last_visit','gender','country_name')
    search_fields = ('email','contact_number')

    readonly_fields = ('last_visit',)
    filter_horizontal = ()
    list_filter = ('email','first_name')

    fieldsets = ()

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','contact_number','password1','password2'),

        }),
    )

    ordering = ('email',)


admin.site.register(MyUser,MyUserAdmin)


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('person','email_code','youtube_link','instagram_link','linkedin_link','type_of_youtube','youtube_subscriber','instagram_followers','low_Budget','high_Budget')


@admin.register(Brand)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('person','company_name','company_profile_link','company_official_email')