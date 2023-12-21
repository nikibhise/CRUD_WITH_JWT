from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

gender_choices = [('male', 'male'), ('female', 'female'), ('other', 'other')]

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models. CharField(max_length=10, choices=gender_choices)
    address = models.TextField()
    city = models.CharField(max_length=20)
    contact_no = PhoneNumberField(region="IN")
    aadharcard_no = models.CharField(max_length=50)
    email = models.EmailField()

