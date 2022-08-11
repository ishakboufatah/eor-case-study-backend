from rest_framework import serializers
from .models import CaseStudies

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseStudies
        fields = ('CaseStudies_id', 'Field', 'Pool_Name','summary','image1','image2','image3',
        'image4','image5','image6','Formation','country','EOR_Type','Flood_Type','Number_of_Wells',
        'Number_of_EOR_Injectors','Number_of_EOR_Producers','Discovery_Date','EOR_start_year',
        'Secondary_Recovery','EOR_1','EOR_2','EOR_3','EOR_4','Depth_m','Average_Pay_Thickness_m',
        'Average_Permeability_md','Average_Porosity','Water_Saturation','Lithology','Initial_Pressure_kPa',
        'Initial_Temperature_C','Oil_Gravity_API','Oil_Density_kgm3','Oil_Viscosity_15C_cp',
        'Oil_Viscosity_Tr_cp','Salinity_of_Formation_Water_ppm','Presence_of_Natural_Fractures',
        'Presence_of_Gas_Cap','Area_of_Project_ha','Primary_Recovery_Factor_fraction',
        'Incremental_WF_Recovery_Factor_fraction','Incremental_EOR_Recovery_Factor_fraction',
        'Total_Recovery_Factor_fraction','OOIP_E3m3','Remaining_Oil_in_Place_E3m3_after_Primary_EOR_Recovery',
        'Remaining_Recoverable_Reserves_E3m3')