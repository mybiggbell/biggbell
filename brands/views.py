from django.shortcuts import render , redirect , HttpResponseRedirect
from userauth.models import Creator , Brand
from .models import Project , Project_Approval
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.


@login_required(login_url='login_user')
def brand_dashboard(request):
    context = {}
    context['creators'] = Creator.objects.all()
    if request.method == 'POST':
        min_value = request.POST.get('min_value')
        max_value = request.POST.get('max_value')
        catergory = request.POST.get('catergory')
        print(min_value=="")
        print(max_value=="")
        print(catergory=="")
        if min_value!="":
            context['creators'] = context['creators'].filter(low_Budget=min_value)
        if max_value!="":
            context['creators'] = context['creators'].filter(high_Budget=max_value)
        if catergory!="":
            context['creators'] = context['creators'].filter(type_of_youtube__icontains=catergory)
    
    return render(request,'brands/brand_dashboard.html',context)

@login_required(login_url='login_user')
def post_a_project(request):
    # here to collect all details about project
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        detail_about_project = request.POST.get('detail_about_project')
        total_cost = request.POST.get('total_cost')
        project_file = request.FILES.get('project_file')
        brand = Brand.objects.get(person=request.user)
        project = Project(project_brand=brand,project_name=project_name,detail_about_project=detail_about_project,total_cost=total_cost,project_file=project_file)
        project.save()
        # request.session['project_id'] = project.id
        # request.session['total_cost'] = total_cost*100000
        return HttpResponseRedirect('/payment-page'+'?project_id='+str(project.id)+'&payment='+str(total_cost))
    
    return render(request,'brands/post_a_project.html')

@login_required(login_url='login_user')
def payment_page(request):
     
    amount = int(request.GET.get('payment'))*100000
    project  = Project.objects.get(id=int(request.GET.get('project_id')))
    print(project)
    print(type(amount))
    # if request.method=='POST':
    if amount is None:
        return redirect('login_user')
    name = request.user.email
    print(name)
    client = razorpay.Client(auth=('rzp_test_Fxuz76qL0LQ11W','EVESIgFY73OXpcN6hbWyrycC'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    project.payment_id = payment['id']
    project.save()
    print(payment)
    return render(request,'brands/payment.html',{'payment':payment,'name':name,'amount':amount,'project':project})

@csrf_exempt
def success(request):
    print(request.POST)
    project_id = int(request.GET.get('project_id'))
    payment_id =  request.GET.get('payment_id')
    project  = Project.objects.get(id=int(request.GET.get('project_id')))
    if project.payment_id != payment_id:
        return render(request, 'brands/payment.html')
    print(project)
    project.paid = True
    project.save()
    return render(request, 'brands/payment.html',{'is_done':True}) 


@login_required(login_url='login_user')
def creator_profile_see(request,id):
    context ={}
    context['user_data'] = Creator.objects.get(id=id)
    return render(request,'brands/creator_profile.html',context)

@login_required(login_url='login_user')
def project_list(request):
    context = {}
    brand = Brand.objects.get(person=request.user)

    context['projects'] = Project.objects.filter(project_brand=brand)
    print(context['projects'])
    
    return render(request,'brands/project_list.html',context)

@login_required(login_url='login_user')
def project_details(request,id):
    context = {} 
    context['projects'] = Project.objects.get(id=id)
    return render(request,'brands/project_details.html',context)

@login_required(login_url='login_user')
def accept(request,id):
    project = Project_Approval.objects.get(id=id)
    project.is_approval = 'Select'
    project.save()
    return redirect('project_list')
    
@login_required(login_url='login_user')
def complete_done(request,id):
    
    project = Project_Approval.objects.get(id=id)
    project.is_approval = 'complete'
    project.save()
    return redirect('project_list')

@login_required(login_url='login_user')
def creator_profile_for_brand(request , id):
    context = {}
    context['user_data'] = Creator.objects.get(id=id)
    print(context['user_data'])
    # context['project_count'] = Project_Approval.objects.filter(creator=context['user_data']).count()
    # print(context['project_count'])
    return render(request,'brands/creator_profile_brand.html',context)

@login_required(login_url='login_user')
def brands_profile(request):
    
    return render(request,'brands/brands_profile.html')