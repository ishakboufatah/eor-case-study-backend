# Generated by Django 3.2.8 on 2022-08-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0037_rename_joincasestudies_id_joincasestudies_casestudies_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='joincasestudies',
            name='area_of_project_ha',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='average_pay_thickness_m',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='average_permeability_md',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='average_porosity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='depth_m',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='discovery_date',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='eor_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='eor_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='eor_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='eor_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='eor_start_year',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='flood_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='formation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='image6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='incremental_eor_recovery_factor_fraction',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='incremental_wf_recovery_factor_fraction',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='initial_pressure_kpa',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='initial_temperature_c',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='lithology',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='number_of_eor_injectors',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='number_of_eor_producers',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='number_of_wells',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='oil_density_kgm3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='oil_gravity_API',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='oil_viscosity_15c_cp',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='oil_viscosity_tr_cp',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='ooip_e3m3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='pool_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='presence_of_gas_cap',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='presence_of_natural_fractures',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='primary_recovery_factor_fraction',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='remaining_oil_in_place_e3m3_after_primary_eor_recovery',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='remaining_recoverable_reserves_e3m3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='salinity_of_formation_water_ppm',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='secondary_recovery',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='summary',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='total_recovery_factor_fraction',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='joincasestudies',
            name='water_saturation',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]