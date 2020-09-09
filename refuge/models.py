from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Refuge(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    ROLE_CHOICES = [
        ('ADM', 'Admin'),
        ('VET', 'Veterinarian'),
        ('ASI', 'Assistant'),
    ]
    phone = models.CharField(max_length=20)
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default="ASI",
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refuge = models.ForeignKey(Refuge,
                               related_name="employees",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Animal(models.Model):
    breed = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True)
    models.BooleanField(default=False)
    owner = models.CharField(max_length=50, null=True)
    refuge = models.ForeignKey(Refuge,
                               related_name="animals",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)