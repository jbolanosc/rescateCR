from rest_framework import serializers
from .models import Refuge, Animal, Employee


class RefugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuge
        fields = ('id', 'name', 'address', 'email', 'phone', 'state',
                  'created_at')


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'breed', 'name', 'owner', 'created_at')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'phone', 'email', 'role', 'created_at')