
#from httplib2 import Authentication

from urllib import request
from .models import CaseStudies,Country,JoinCaseStudies
from .serializers import TaskSerializer,CountrySerializer,JoinCaseStudiesSerializer
import EORDatabase.urls  

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = CaseStudies.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['casestudies_id','country_id','eor_subtype_id']
    search_fields =  ['casestudies_id','country_id','eor_subtype_id']
    ordering_fields = ['casestudies_id','country_id','eor_subtype_id']


class JoinMiscibleCaseStudiesViewSet(viewsets.ModelViewSet): 
    permission_classes =[DjangoModelPermissions]
    
    queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
    serializer_class = JoinCaseStudiesSerializer




class ListJoinMiscibleViewSet(viewsets.ModelViewSet): 
    
    permission_classes =[DjangoModelPermissions] 
    serializer_class=JoinCaseStudiesSerializer
    def get_queryset(self,**kwargs):
        country= self.request.query_params.get('country')
        eortype= self.request.query_params.get('eortype')
        print(self.request.query_params)
        print(self.request.query_params.get('tech'))
        print(self.request.query_params.get('c'))
        print(self.request.query_params.get('tech')=='Canada')
        
        # tech=None
        
        if (country is not None) and (eortype is not None):
            queryset=JoinCaseStudies.objects.raw("""SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where ( casestudies_eortechniques.eor_type = %(eortype)s and casestudies_country.country= %(country)s)  ORDER BY casestudies_casestudies.casestudies_id;""",params={'country':country ,'eortype':eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        elif (country is not None) :
            queryset=JoinCaseStudies.objects.raw("""SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_country.country= %(country)s ORDER BY casestudies_casestudies.casestudies_id;""",params={'country':country ,'eortype':eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        if (eortype is not None):
            queryset=JoinCaseStudies.objects.raw("""SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = %(eortype)s  ORDER BY casestudies_casestudies.casestudies_id;""",params={'country':country ,'eortype':eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        else:
            queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        
   
        
    

class JoinChemicalCaseStudiesViewSet(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissions]
    queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id  where casestudies_eortechniques.eor_type = 'Chemical EOR' ORDER BY casestudies_casestudies.casestudies_id;")
    serializer_class = JoinCaseStudiesSerializer
