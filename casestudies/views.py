
#from httplib2 import Authentication

from urllib import request
from .models import CaseStudies, Country, JoinCaseStudies, EORTechniques,Rangeperm,Rangepor,RangeRT,RangeSal,RangeVisc,WWdisrtribution
from .serializers import TaskSerializer, CountrySerializer, JoinCaseStudiesSerializer, EORTechniquesTypeSerializer,RangepermSerializer,RangeporSerializer,RangeRTSerializer,RangeSalSerializer,RangeViscSerializer,WWdisrtributionSerializer
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
      count(1) as count FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id=casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id=casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id=casestudies_country.country_id WHERE eor_start_year IS NOT NULL AND eor_type IS NOT NULL AND country IS NOT NULL GROUP BY eor_start_year,eor_type,country 
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
                                            WHEN casestudies_casestudies.average_permeability_md > 10000 THEN '> 10000 (md)'
                                            else 'OTHERS' END AS rangeperm, count(1) as count FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id=casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id=casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id=casestudies_country.country_id GROUP BY rangeperm,eor_type
                                           """)
    serializer_class = RangepermSerializer


class RangeporViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = Rangepor.objects.raw("""  Select 1 as id ,casestudies_eortechniques.eor_type as eor_type ,CASE WHEN casestudies_casestudies.average_porosity <= 0.05 THEN '[0 - 0.05]'
                                            WHEN casestudies_casestudies.average_porosity > 0.05 and casestudies_casestudies.average_porosity <= 0.1 THEN ']0.05 - 0.1]'
                                            WHEN casestudies_casestudies.average_porosity > 0.1 and casestudies_casestudies.average_porosity <= 0.15 THEN ']0.1 - 0.15]'
                                            WHEN casestudies_casestudies.average_porosity > 0.15 and casestudies_casestudies.average_porosity <= 0.2 THEN ']0.15- 0.2]'
                                            WHEN casestudies_casestudies.average_porosity > 0.2 and casestudies_casestudies.average_porosity <= 0.25 THEN ']0.2 - 0.25]'
                                            WHEN casestudies_casestudies.average_porosity > 0.25 and casestudies_casestudies.average_porosity <= 0.3 THEN ']0.25 - 0.3]'
                                            WHEN casestudies_casestudies.average_porosity > 0.3 and casestudies_casestudies.average_porosity <= 0.35 THEN ']0.3 - 0.35]'
                                            WHEN casestudies_casestudies.average_porosity > 0.35 and casestudies_casestudies.average_porosity <= 0.4 THEN ']0.35 - 0.4]'
                                            WHEN casestudies_casestudies.average_porosity > 0.4 and casestudies_casestudies.average_porosity <= 0.45 THEN ']0.4 - 0.45]'
                                            WHEN casestudies_casestudies.average_porosity > 0.45 and casestudies_casestudies.average_porosity <= 0.5 THEN ']0.45 - 0.5]'
                                            WHEN casestudies_casestudies.average_porosity > 0.5 and casestudies_casestudies.average_porosity <= 0.55 THEN ']0.5 - 0.55]'
                                            WHEN casestudies_casestudies.average_porosity > 0.55 and casestudies_casestudies.average_porosity <= 0.6 THEN ']0.55 - 0.6]'
                                            WHEN casestudies_casestudies.average_porosity > 0.6 and casestudies_casestudies.average_porosity <= 0.65 THEN ']0.6 - 0.65]'
                                            WHEN casestudies_casestudies.average_porosity > 0.65 and casestudies_casestudies.average_porosity <= 0.7 THEN ']0.65 - 0.7]'
                                            WHEN casestudies_casestudies.average_porosity > 0.7 and casestudies_casestudies.average_porosity <= 0.75 THEN ']0.7 - 0.75]'
                                            WHEN casestudies_casestudies.average_porosity > 0.75 and casestudies_casestudies.average_porosity <= 0.8 THEN ']0.75 - 0.8]'
                                            WHEN casestudies_casestudies.average_porosity > 0.8 and casestudies_casestudies.average_porosity <= 0.85 THEN ']0.8 - 0.85]'
                                            WHEN casestudies_casestudies.average_porosity > 0.85 and casestudies_casestudies.average_porosity <= 0.9 THEN ']0.85 - 0.9]'
                                            WHEN casestudies_casestudies.average_porosity > 0.9 and casestudies_casestudies.average_porosity <= 0.95 THEN ']0.9 - 0.95]'
                                            WHEN casestudies_casestudies.average_porosity > 0.95 and casestudies_casestudies.average_porosity <= 1 THEN ']0.95 - 1]'
                                            else 'OTHERS' END AS rangepor, count(1) as count FROM casestudies_casestudies left JOIN casestudies_eorsubtype ON casestudies_casestudies.eor_subtype_id=casestudies_eorsubtype.eor_subtype_id left JOIN casestudies_eortechniques ON casestudies_eorsubtype.eor_techniques_id=casestudies_eortechniques.eor_techniques_id left JOIN casestudies_country on casestudies_casestudies.country_id=casestudies_country.country_id GROUP BY rangepor,eor_type
                                           """)
    serializer_class = RangeporSerializer
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
