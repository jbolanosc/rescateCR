from .models import Refuge, Animal, Employee
from .serializers import RefugeSerializer, AnimalSerializer, EmployeeSerializer
from rest_framework import generics


class RefugeListCreate(generics.ListCreateAPIView):
    queryset = Refuge.objects.all()
    serializer_class = RefugeSerializer
