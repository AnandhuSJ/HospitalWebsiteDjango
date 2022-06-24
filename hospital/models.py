from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class appointment(models.Model):
    deid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, default='')
    mail = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    make_an_appointment = models.CharField(max_length=100)
    message = models.CharField(max_length=800)
class sub_e_mail(models.Model):
    e_id=models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
class contact(models.Model):
    deid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, default='')
    Email = models.CharField(max_length=100)
    subject = PhoneNumberField(null=False, blank=False, unique=True)
    message = models.CharField(max_length=800)


class contact1(models.Model):
    deid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    subject = models.CharField(max_length=900)
    message = models.CharField(max_length=800)