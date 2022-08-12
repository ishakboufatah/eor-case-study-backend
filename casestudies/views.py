
#from httplib2 import Authentication

from .models import CaseStudies,Country
from .serializers import TaskSerializer,CountrySerializer

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

class CountryViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = CaseStudies.objects.all()
    serializer_class = TaskSerializer
