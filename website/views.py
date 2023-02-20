from django.shortcuts import render , redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        if request.user.is_creator:
            return redirect('creator_dashboard')
        else:
            return redirect('brand_dashboard')
    return render(request,'website/index.html')

def how_it_work(request):
    return render(request,'website/how_it_work.html')