from django.db import models


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
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default="ASI",
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Animal(models.Model):
    breed = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True)
    owner = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)