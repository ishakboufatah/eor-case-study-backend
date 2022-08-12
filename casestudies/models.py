from django.db import models


class Country(models.Model):
    Country_id = models.BigAutoField(primary_key=True)
    Country = models.CharField(max_length=100)  
    def __str__(self) :
        return f"{self.Country}"

class EORTechniques(models.Model):
    EOR_Techniques_id = models.BigAutoField(primary_key=True)
    EOR_Type = models.CharField(max_length=100,null=False)  
    EOR_Type_Description = models.CharField(max_length=1000)
    def __str__(self) :
        return f"{self.EOR_Type}"

class EORsubType(models.Model):
    EOR_SubType_id = models.BigAutoField(primary_key=True)
    EOR_Type =  models.ForeignKey('EORTechniques', models.DO_NOTHING, db_column='EOR_Type',null=False) 
    EOR_Sub_Type =  models.CharField(max_length=100)
    EOR_Sub_Type_Description = models.CharField(max_length=1000)
    def __str__(self) :
        return f"{self.EOR_Type} - {self.EOR_Sub_Type}"
class Lithology(models.Model):
    Lithology_id = models.BigAutoField(primary_key=True)
    Lithology = models.CharField(max_length=100)  
    def __str__(self) :
        return f"{self.Lithology}"

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
    CaseStudies_id = models.BigAutoField(primary_key=True)
    Field = models.CharField(max_length=50)
    Pool_Name = models.CharField(max_length=50,blank=True)
    summary = models.TextField(max_length=10000,blank=True)
    image1 = models.ImageField(upload_to='image/',null=True,blank=True)
    image2 = models.ImageField(upload_to='image/',null=True,blank=True)
    image3 = models.ImageField(upload_to='image/',null=True,blank=True)
    image4 = models.ImageField(upload_to='image/',null=True,blank=True)
    image5 = models.ImageField(upload_to='image/',null=True,blank=True)
    image6 = models.ImageField(upload_to='image/',null=True,blank=True)
    Formation = models.CharField(max_length=50,null=True,blank=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, db_column='Country',null=True,blank=True)
    EOR_Type = models.ForeignKey('EORsubType', models.DO_NOTHING, db_column='EOR_Type',related_name='EORType',null=True,blank=True)
    Flood_Type = models.CharField(max_length=15, choices=Flood_Type_CHOICES,null=True,blank=True)
    Number_of_Wells = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Number_of_EOR_Injectors = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Number_of_EOR_Producers = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Discovery_Date= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    EOR_start_year = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Secondary_Recovery =  models.CharField(max_length=50,null=True,blank=True)
    EOR_1 = models.CharField(max_length=50,null=True,blank=True)
    EOR_2 = models.CharField(max_length=50,null=True,blank=True)
    EOR_3 = models.CharField(max_length=50,null=True,blank=True)
    EOR_4 = models.CharField(max_length=50,null=True,blank=True)
    Depth_m = models.DecimalField(max_digits=5, decimal_places=1,null=True,blank=True)
    Average_Pay_Thickness_m = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Average_Permeability_md = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Average_Porosity = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Water_Saturation = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Lithology = models.ForeignKey('Lithology', models.DO_NOTHING, db_column='Lithology',blank=True)
    Initial_Pressure_kPa = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Initial_Temperature_C = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Oil_Gravity_API = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Oil_Density_kgm3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Oil_Viscosity_15C_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Oil_Viscosity_Tr_cp = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Salinity_of_Formation_Water_ppm = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Presence_of_Natural_Fractures = models.CharField(max_length=15, choices=Yes_No_CHOICES,null=True,blank=True)
    Presence_of_Gas_Cap = models.CharField(max_length=10, choices=Yes_No_CHOICES,null=True,blank=True)
    Area_of_Project_ha = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Primary_Recovery_Factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Incremental_WF_Recovery_Factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Incremental_EOR_Recovery_Factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Total_Recovery_Factor_fraction= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    OOIP_E3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Remaining_Oil_in_Place_E3m3_after_Primary_EOR_Recovery = models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    Remaining_Recoverable_Reserves_E3m3= models.DecimalField(max_digits=10, decimal_places=4,null=True,blank=True)
    


    


    def __str__(self) :
        return f"{self.Field}"

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
class IMAGE(models.Model):

    image1 = models.ImageField(upload_to='image/',null=True,)