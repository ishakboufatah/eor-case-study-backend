
#from httplib2 import Authentication

from .models import CaseStudies,Country
from .serializers import TaskSerializer,CountrySerializer

from rest_framework import viewsets,filters
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend

class CountryViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends= [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields= ['CaseStudies_id','country','EOR_Type']
    search_fields= ['CaseStudies_id','country','EOR_Type']
    ordering_fields= ['CaseStudies_id','country','EOR_Type']

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = CaseStudies.objects.all()
    serializer_class = TaskSerializer
