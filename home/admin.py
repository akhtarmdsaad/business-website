from django.contrib import admin

from home.models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Material)
admin.site.register(Order)