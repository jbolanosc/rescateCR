from rest_framework import serializers
from .models import Refuge, Animal, Employee


class RefugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refuge
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'