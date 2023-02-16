from django.shortcuts import render
from brands.models import Project , Project_Approval 
from userauth.models import Creator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_user')
def creator_dashboard(request):
    context = {}
    projects = Project.objects.all()
    print(projects)
    context['projects'] = projects
    return render(request,'creator_dashboard.html' , context)

@login_required(login_url='login_user')
def apply_project(request,id):
    context = {}
    project = Project.objects.get(id=id)
    creator = Creator.objects.get(person=request.user)
    is_already_approval = Project_Approval.objects.filter(creator=creator,project=project).exists()
    context['is_already_approval'] = is_already_approval
    context['project'] = project
    if request.method == 'POST':
        if is_already_approval==False:
            creator_note = request.POST.get('creator_note')
            # print(creator)
            # print(creator_note)
            data = Project_Approval(project=project,creator=creator,creator_note=creator_note)
            data.save()
    print(is_already_approval)
    return render(request,'apply_project.html' , context)
 
@login_required(login_url='login_user')
def creator_profile(request):
    context = {}
    context['user_data'] = Creator.objects.get(person=request.user)
    print(context['user_data'])
    context['project_count'] = Project_Approval.objects.filter(creator=context['user_data']).count()
    print(context['project_count'])
    return render(request,'creator_profile.html',context)


@login_required(login_url='login_user')
def cretor_project_all(request):
    context = {}
    context['user_data'] = Creator.objects.get(person=request.user)
    context['projects'] = Project_Approval.objects.filter(creator=context['user_data'])
    print(context['projects'])
    return render(request,'cretor_project_all.html',context)

