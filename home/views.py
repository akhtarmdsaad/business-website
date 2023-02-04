from django.shortcuts import render,HttpResponse

# 7855044379
# rehana

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def services(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
