from refuge.models import Animal, Refuge, Employee
from rest_framework import viewsets, permissions
from .serializers import RefugeSerializer, AnimalSerializer, EmployeeSerializer


class RefugeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Refuge.objects.all()
    serializer_class = RefugeSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return self.request.user.employee.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)