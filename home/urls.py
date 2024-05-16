from django.contrib import admin
from django.urls import path,include

from home import views
urlpatterns = [
    path("",views.index,name = "home"),
    path("services/",views.services, name = "services"),
    path("about/",views.about, name = "about"),
    path("contact/",views.contact, name = "contact"),
    path("order/",views.order, name = "order"),
    path("see_order/",views.see_order_details, name = "see_order"),
    path("see_contact/",views.see_contact_details, name = "see_contact")
]
