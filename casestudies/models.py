from django.db import models


class Country(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=100)  
    def __str__(self) :
        return f"{self.country}"

class EORTechniques(models.Model):
    eor_techniques_id = models.BigAutoField(primary_key=True)
    eor_type = models.CharField(max_length=100,null=False)  
    eor_type_description = models.CharField(max_length=1000)
    def __str__(self) :
        return f"{self.eor_type}"

class EORsubType(models.Model):
    eor_subtype_id = models.BigAutoField(primary_key=True)
    eor_type =  models.ForeignKey('EORTechniques', models.DO_NOTHING, db_column='eor_techniques_id',null=False) 
    eor_sub_type =  models.CharField(max_length=100)
    eor_sub_type_Description = models.CharField(max_length=1000)
    def __str__(self) :
        return f"{self.eor_type} - {self.eor_sub_type}"
class Lithology(models.Model):
    lithology_id = models.BigAutoField(primary_key=True)
    lithology = models.CharField(max_length=100)  
    def __str__(self) :
        return f"{self.lithology}"

class CaseStudies(models.Model):
    VERTICAL = 'Vertical'
    HORIZONTAL = 'Horizontal'
    COMBINATION = 'Combination'
    YES ='Yes'
    NO = 'No'
    Yes_No_CHOICES =(
        (YES, 'Yes'),
        (NO, 'No')
    )

    Flood_Type_CHOICES = (
        (VERTICAL, 'Vertical'),
        (HORIZONTAL, 'Horizontal'),
        (COMBINATION, 'Combination')
    )
    casestudies_id = models.BigAutoField(primary_key=True)
    field = models.CharField(max_length=50)
    pool_name = models.CharField(max_length=50,blank=True)
    summary = models.TextField(max_length=10000,blank=True)
    formation = models.CharField(max_length=50,null=True,blank=True)
    country_id = models.ForeignKey('Country', models.DO_NOTHING, db_column='country_id',null=True,blank=True)
    eor_subtype_id = models.ForeignKey('EORsubType', models.DO_NOTHING, db_column='eor_subtype_id',null=True,blank=True)
    flood_type = models.CharField(max_length=15, choices=Flood_Type_CHOICES,null=True,blank=True)
    number_of_wells = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    number_of_eor_injectors = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    number_of_eor_producers = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    discovery_date= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    eor_start_year = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    secondary_recovery =  models.CharField(max_length=50,null=True,blank=True)
    eor_1 = models.CharField(max_length=50,null=True,blank=True)
    eor_2 = models.CharField(max_length=50,null=True,blank=True)
    eor_3 = models.CharField(max_length=50,null=True,blank=True)
    eor_4 = models.CharField(max_length=50,null=True,blank=True)
    depth_m = models.DecimalField(max_digits=5, decimal_places=1,null=True,blank=True)
    average_pay_thickness_m = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    average_permeability_md = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    average_porosity = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    water_saturation = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    lithology = models.ForeignKey('Lithology', models.DO_NOTHING, db_column='lithology',null=True,blank=True)
    initial_pressure_kpa = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    initial_temperature_c = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_gravity_API = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_density_kgm3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_viscosity_15c_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_viscosity_tr_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    salinity_of_formation_water_ppm = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    presence_of_natural_fractures = models.CharField(max_length=15, choices=Yes_No_CHOICES,null=True,blank=True)
    presence_of_gas_cap = models.CharField(max_length=10, choices=Yes_No_CHOICES,null=True,blank=True)
    area_of_project_ha = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    primary_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    incremental_wf_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    incremental_eor_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    total_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    ooip_e3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    remaining_oil_in_place_e3m3_after_primary_eor_recovery = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    remaining_recoverable_reserves_e3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    


    


    def __str__(self) :
        return f"{self.field}  {self.pool_name}"

class JoinCaseStudies(models.Model):
    casestudies_id = models.BigAutoField(primary_key=True)
    field = models.CharField(max_length=50)
    pool_name = models.CharField(max_length=50,blank=True)
    summary = models.TextField(max_length=10000,blank=True)
    formation = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,blank=True)
    eor_type = models.CharField(max_length=50)
    eor_sub_type = models.CharField(max_length=50)
    flood_type = models.CharField(max_length=50,blank=True)
    number_of_wells = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    number_of_eor_injectors = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    number_of_eor_producers = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    discovery_date= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    eor_start_year = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    secondary_recovery =  models.CharField(max_length=50,null=True,blank=True)
    eor_1 = models.CharField(max_length=50,null=True,blank=True)
    eor_2 = models.CharField(max_length=50,null=True,blank=True)
    eor_3 = models.CharField(max_length=50,null=True,blank=True)
    eor_4 = models.CharField(max_length=50,null=True,blank=True)
    depth_m = models.DecimalField(max_digits=5, decimal_places=1,null=True,blank=True)
    average_pay_thickness_m = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    average_permeability_md = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    average_porosity = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    water_saturation = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    lithology = models.CharField(max_length=50,blank=True)
    initial_pressure_kpa = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    initial_temperature_c = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_gravity_API = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_density_kgm3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_viscosity_15c_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    oil_viscosity_tr_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    salinity_of_formation_water_ppm = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    presence_of_natural_fractures = models.CharField(max_length=50,blank=True)
    presence_of_gas_cap = models.CharField(max_length=50,blank=True)
    area_of_project_ha = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    primary_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    incremental_wf_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    incremental_eor_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    total_recovery_factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    ooip_e3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    remaining_oil_in_place_e3m3_after_primary_eor_recovery = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    remaining_recoverable_reserves_e3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)

    
    def __str__(self) :
        return f"{self.field}"
    

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
class IMAGE(models.Model):

    image1 = models.ImageField(upload_to='image/',null=True,)

class Rangeperm(models.Model):
    rangeperm= models.CharField(max_length=50,blank=True)
    count= models.DecimalField(max_digits=10, decimal_places=0,null=True,blank=True)
    def __str__(self) :
        return f"{self.rangeperm}"