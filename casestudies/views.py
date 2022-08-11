
#from httplib2 import Authentication

from .models import CaseStudies
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = CaseStudies.objects.all()
    serializer_class = TaskSerializer
