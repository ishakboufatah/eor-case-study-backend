
#from httplib2 import Authentication

from urllib import request
from .models import CaseStudies, Country, JoinCaseStudies, EORTechniques,Rangeperm,WWdisrtribution
from .serializers import TaskSerializer, CountrySerializer, JoinCaseStudiesSerializer, EORTechniquesTypeSerializer,RangepermSerializer,WWdisrtributionSerializer
import EORDatabase.urls

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class EORTechniquesViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = EORTechniques.objects.all()
    serializer_class = EORTechniquesTypeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = CaseStudies.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['casestudies_id', 'country_id', 'eor_subtype_id']
    search_fields = ['casestudies_id', 'country_id', 'eor_subtype_id']
    ordering_fields = ['casestudies_id', 'country_id', 'eor_subtype_id']


class JoinMiscibleCaseStudiesViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
    serializer_class = JoinCaseStudiesSerializer


class WWdisrtributionViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = WWdisrtribution.objects.raw("""  Select casestudies_casestudies.casestudies_id as casestudies_id,casestudies_casestudies.eor_start_year as eor_start_year ,casestudies_eortechniques.eor_type as eor_type, casestudies_country.country as country,
      count(1) as count FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id=casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id=casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id=casestudies_country.country_id GROUP BY eor_start_year,eor_type,country
                                           """)
    serializer_class = WWdisrtributionSerializer


class RangepermViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = Rangeperm.objects.raw("""  Select 1 as id ,casestudies_eortechniques.eor_type as eor_type ,CASE WHEN casestudies_casestudies.average_permeability_md <= 50 THEN '[0 - 50] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 50 and casestudies_casestudies.average_permeability_md <= 100 THEN ']50 - 100] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 100 and casestudies_casestudies.average_permeability_md <= 150 THEN ']100 - 150] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 150 and casestudies_casestudies.average_permeability_md <= 200 THEN ']150 - 200] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 200 and casestudies_casestudies.average_permeability_md <= 250 THEN ']200 - 250] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 250 and casestudies_casestudies.average_permeability_md <= 300 THEN ']250 - 300] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 300 and casestudies_casestudies.average_permeability_md <= 350 THEN ']300 - 350] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 350 and casestudies_casestudies.average_permeability_md <= 400 THEN ']350 - 400] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 400 and casestudies_casestudies.average_permeability_md <= 450 THEN ']400 - 450] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 450 and casestudies_casestudies.average_permeability_md <= 500 THEN ']450 - 500] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 500 and casestudies_casestudies.average_permeability_md <= 600 THEN ']500 - 600] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 600 and casestudies_casestudies.average_permeability_md <= 700 THEN ']600 - 700] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 700 and casestudies_casestudies.average_permeability_md <= 800 THEN ']700 - 800] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 800 and casestudies_casestudies.average_permeability_md <= 900 THEN ']800 - 900] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 900 and casestudies_casestudies.average_permeability_md <= 1000 THEN ']900 - 1000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 1000 and casestudies_casestudies.average_permeability_md <= 2000 THEN ']1000 - 2000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 2000 and casestudies_casestudies.average_permeability_md <= 3000 THEN ']2000 - 3000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 3000 and casestudies_casestudies.average_permeability_md <= 4000 THEN ']3000 - 4000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 4000 and casestudies_casestudies.average_permeability_md <= 5000 THEN ']4000 - 5000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 5000 and casestudies_casestudies.average_permeability_md <= 6000 THEN ']5000 - 6000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 6000 and casestudies_casestudies.average_permeability_md <= 7000 THEN ']6000 - 7000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 7000 and casestudies_casestudies.average_permeability_md <= 8000 THEN ']7000 - 8000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 8000 and casestudies_casestudies.average_permeability_md <= 9000 THEN ']8000 - 9000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 9000 and casestudies_casestudies.average_permeability_md <= 10000 THEN ']9000 - 10000] (md)'
                                            WHEN casestudies_casestudies.average_permeability_md > 10000 and casestudies_eortechniques.eor_type='Miscible EOR' THEN '> 10000 (md)'
                                            else 'OTHERS' END AS rangeperm, count(1) as count FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id=casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id=casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id=casestudies_country.country_id GROUP BY rangeperm,eor_type
                                           """)
    serializer_class = RangepermSerializer

class ListJoinMiscibleViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    serializer_class = JoinCaseStudiesSerializer

    def get_queryset(self, **kwargs):
        country = self.request.query_params.get('country')
        eortype = self.request.query_params.get('eortype')
        print(self.request.query_params)
        print(self.request.query_params.get('tech'))
        print(self.request.query_params.get('c'))
        print(self.request.query_params.get('tech') == 'Canada')

        # tech=None

        if (country is not None) and (eortype is not None):
            queryset = JoinCaseStudies.objects.raw(
                """SELECT *FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where ( casestudies_eortechniques.eor_type = %(eortype)s and casestudies_country.country= %(country)s)  ORDER BY casestudies_casestudies.casestudies_id;""", params={'country': country, 'eortype': eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        elif (country is not None):
            queryset = JoinCaseStudies.objects.raw(
                """SELECT *FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_country.country= %(country)s ORDER BY casestudies_casestudies.casestudies_id;""", params={'country': country, 'eortype': eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        if (eortype is not None):
            queryset = JoinCaseStudies.objects.raw(
                """SELECT *FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = %(eortype)s  ORDER BY casestudies_casestudies.casestudies_id;""", params={'country': country, 'eortype': eortype})
            # queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id where  casestudies_eortechniques.eor_type = 'Miscible EOR'  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset
        else:
            queryset = JoinCaseStudies.objects.raw("SELECT *FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id = casestudies_country.country_id  ORDER BY casestudies_casestudies.casestudies_id;")
            return queryset


class JoinChemicalCaseStudiesViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = JoinCaseStudies.objects.raw("SELECT *FROM public.casestudies_casestudies left JOIN public.casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id = casestudies_eorsubtype.eor_subtype_id left JOIN public.casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id = casestudies_eortechniques.eor_techniques_id  where casestudies_eortechniques.eor_type = 'Chemical EOR' ORDER BY casestudies_casestudies.casestudies_id;")
    serializer_class = JoinCaseStudiesSerializer
