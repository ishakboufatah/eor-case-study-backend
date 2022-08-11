from rest_framework import serializers
from .models import CaseStudies

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseStudies
        fields = ('CaseStudies_id', 'Field', 'Pool_Name')