from django.contrib import admin
from .models import *
class AdminCustomer(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email'

    ]

# Register your models here.
admin.site.register(Customer,AdminCustomer)
