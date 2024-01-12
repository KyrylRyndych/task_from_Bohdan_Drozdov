from .models import Team, Employee
from rest_framework import viewsets, permissions
from .serializers import TeamSerializer, EmployeeSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeamSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer
