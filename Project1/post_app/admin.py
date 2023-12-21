from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'address', 'city', 'contact_no', 'aadharcard_no', 'email')

