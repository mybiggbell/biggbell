from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import login, authenticate, logout
from .models import MyUser , Creator , Brand
import uuid
from django.contrib import messages
from .forms import UserRegistration , LoginForm , CreatorFrom ,BrandFrom
from django.contrib.auth import authenticate, login
# Create your views here.



def login_user(request):
    # brands and creators also login using this view
     
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_creator:
                    return redirect('creator_dashboard')
                else:
                    return redirect('brand_dashboard')
            else:
                messages.error(request,"Email or Password Invalid..")
                return redirect('login_user')
           
    return render(request,'login-page.html')

 

def creator_register(request):
    context = {}
    context['register_form'] = UserRegistration() 
    if request.method == 'POST':
        
        fm1 = UserRegistration(request.POST)
        if fm1.is_valid():
            user = fm1.save()
            user.is_creator = True
            user.save()
            request.session['user-id'] = user.id
            return redirect('next_register_cretor')
    else:
        print("get")
   
    return render(request,'creator-register.html',context)

def next_register_cretor(request):
    context = {} 
    context['register_form1'] = CreatorFrom()
    user_id = request.session.get('user-id', False)
    if user_id==False:
        return redirect('login_user')
    get_user = MyUser.objects.get(id=user_id)
    if Creator.objects.filter(person=get_user).exists():
        return redirect('login_user')
    if request.method == 'POST':
       
        fm = CreatorFrom(request.POST,request.FILES)
        if fm.is_valid():
            profile_img = fm.cleaned_data['profile_img']
            youtube_name = fm.cleaned_data['youtube_name']
            instagram_name = fm.cleaned_data['instagram_name']
            youtube_link = fm.cleaned_data['youtube_link']
            instagram_link = fm.cleaned_data['instagram_link']
            linkedin_link = fm.cleaned_data['linkedin_link']
            type_of_youtube = fm.cleaned_data['type_of_youtube']
            youtube_subscriber = fm.cleaned_data['youtube_subscriber']
            instagram_followers = fm.cleaned_data['instagram_followers']
            low_Budget = fm.cleaned_data['low_Budget']
            high_Budget = fm.cleaned_data['high_Budget']
            data = Creator(person=get_user,profile_img=profile_img,youtube_name=youtube_name,instagram_name=instagram_name,youtube_link=youtube_link,instagram_link=instagram_link,linkedin_link=linkedin_link,type_of_youtube=type_of_youtube,youtube_subscriber=youtube_subscriber,instagram_followers=instagram_followers,low_Budget=low_Budget,high_Budget=high_Budget,email_code=uuid.uuid4())
            data.save()
            messages.success(request,"check Your Email and Verify It")
            return redirect('login_user') 
    return render(request,'next_register_creator.html',context)


def brands_register(request):
    context = {}
    context['register_form'] = UserRegistration() 
    if request.method == 'POST':
        print("===========")
        fm1 = UserRegistration(request.POST)
        if fm1.is_valid():
            user = fm1.save() 
            user.save()
            request.session['user-id'] = user.id
            return redirect('next_register_brand')
    else:
        print("get")
   
    return render(request,'creator-register.html',context)

def next_register_brand(request):
    context = {} 
    context['register_form1'] = BrandFrom()
    user_id = request.session.get('user-id', False)
    if user_id==False:
        return redirect('login_user')
    get_user = MyUser.objects.get(id=user_id)
    if Creator.objects.filter(person=get_user).exists():
        return redirect('login_user')
    if request.method == 'POST':
       
        fm = BrandFrom(request.POST)
        if fm.is_valid():
            company_name = fm.cleaned_data['company_name']
            company_profile_link = fm.cleaned_data['company_profile_link']
            company_official_email = fm.cleaned_data['company_official_email']  
            date = Brand(person=get_user,company_name=company_name,company_official_email=company_official_email,company_profile_link=company_profile_link)
            date.save()
            messages.success(request,"check Your Email and Verify It")
            return redirect('login_user')
        print(fm)
     
    return render(request,'next_register_brand.html',context)

def user_logout(request):
    logout(request)
    return redirect('login_user')
