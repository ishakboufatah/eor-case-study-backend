from rest_framework import serializers
from .models import CaseStudies ,Country,EORTechniques,EORsubType,Lithology,JoinCaseStudies

class EORTechniquesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EORTechniques
        fields = '__all__'
class EORsubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EORsubType
        fields = '__all__'
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    country_id = serializers.SlugRelatedField(slug_field='country', queryset=Country.objects.raw("SELECT * from casestudies_country"))
    eor_subtype_id= serializers.StringRelatedField()
    lithology= serializers.SlugRelatedField(slug_field='lithology', queryset=Lithology.objects.raw("SELECT * from casestudies_lithology"))
    class Meta:
        model = CaseStudies
        fields = ('casestudies_id','field','pool_name','summary','image1','image2','image3','image4','image5','image6','formation',
        'country_id','eor_subtype_id','flood_type','number_of_wells','number_of_eor_injectors','number_of_eor_producers',
        'discovery_date','eor_start_year','secondary_recovery','eor_1','eor_2','eor_3','eor_4',
        'depth_m','average_pay_thickness_m','average_permeability_md','average_porosity','water_saturation',
        'lithology','initial_pressure_kpa','initial_temperature_c','oil_gravity_API','oil_density_kgm3',
        'oil_viscosity_15c_cp','oil_viscosity_tr_cp','salinity_of_formation_water_ppm','presence_of_natural_fractures',
        'presence_of_gas_cap','area_of_project_ha','primary_recovery_factor_fraction','incremental_wf_recovery_factor_fraction',
        'incremental_eor_recovery_factor_fraction','total_recovery_factor_fraction','ooip_e3m3',
        'remaining_oil_in_place_e3m3_after_primary_eor_recovery','remaining_recoverable_reserves_e3m3')
class JoinCaseStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinCaseStudies
        fields ='__all__'

        """
        ('casestudies_id','field','pool_name','summary','image1','image2','image3','image4','image5','image6','formation',
        'country','eor_type','eor_sub_type','flood_type','number_of_wells','number_of_eor_injectors','number_of_eor_producers',
        'discovery_date','eor_start_year','secondary_recovery','eor_1','eor_2','eor_3','eor_4',
        'depth_m','average_pay_thickness_m','average_permeability_md','average_porosity','water_saturation',
        'lithology','initial_pressure_kpa','initial_temperature_c','oil_gravity_API','oil_density_kgm3',
        'oil_viscosity_15c_cp','oil_viscosity_tr_cp','salinity_of_formation_water_ppm','presence_of_natural_fractures',
        'presence_of_gas_cap','area_of_project_ha','primary_recovery_factor_fraction','incremental_wf_recovery_factor_fraction',
        'incremental_eor_recovery_factor_fraction','total_recovery_factor_fraction','ooip_e3m3',
        'remaining_oil_in_place_e3m3_after_primary_eor_recovery','remaining_recoverable_reserves_e3m3')
        """
     
