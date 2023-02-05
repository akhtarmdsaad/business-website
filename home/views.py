from django.shortcuts import redirect, render,HttpResponse

from home.models import Contact
from .forms import OrderForm
# 7855044379
# rehana

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def services(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Order invalid")
        return redirect("order")
    else:
        form = OrderForm()

        return render(request,"order.html",{
            "form":form
        })

def see_contact_details(request):  
    if request.user.is_authenticated:
        contacts = Contact.objects.all()
        context = {
            "contacts":contacts
        }
        return render(request,"see_contact.html",context)
    else:
        return redirect("home")

def contact(request):
    if request.method == "POST":
        # collect form data
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        #validation if required

        obj = Contact(name=name,email=email,message=message)
        obj.save()

        return redirect("contact")
    else:
        return render(request,"contact.html")
