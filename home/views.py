from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from home.models import Contact, Order
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
            name = request.POST["name"]
            phone = request.POST["phone"]
            if not phone.isdigit():
                print("phone:",phone)
                messages.error(request,"Phone no should be integer")
                return redirect("home")
            trips = request.POST["trips"]
            if not trips.isdigit():
                print("trips:",trips)
                messages.error(request,"no of trips should be integer")
                return redirect("home")
            material = form.cleaned_data["materials"]
            payment = form.cleaned_data["payment_mode"]
            address = request.POST["address"]

            obj = Order(name=name,phone=int(phone),address = address,trips=int(trips),materials=material,payment_mode = payment)
            obj.save()
            messages.success(request,"Order Posted Successfully")
        else:
            messages.error(request,"Order invalid")
        return redirect("order")
    else:
        form = OrderForm()

        return render(request,"order.html",{
            "form":form
        })

def see_order_details(request):  
    if request.user.is_authenticated:
        orders = Order.objects.all()
        context = {
            "orders":orders
        }
        return render(request,"see_order.html",context)
    else:
        return redirect("home")

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
        phone = request.POST["phone"]
        message = request.POST["message"]

        #validation if required
        if not("@" in email and "." in email):
            messages.error(request,"Email is not valid")
        obj = Contact(name=name,email=email,message=message)
        obj.save()

        return redirect("contact")
    else:
        return render(request,"contact.html")
