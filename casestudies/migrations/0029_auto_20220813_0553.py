# Generated by Django 3.2.8 on 2022-08-13 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0028_auto_20220813_0553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudies',
            old_name='Oil_Density_kgm3',
            new_name='oil_density_kgm3',
        ),
        migrations.RenameField(
            model_name='casestudies',
            old_name='Oil_Gravity_API',
            new_name='oil_gravity_API',
        ),
        migrations.RenameField(
            model_name='casestudies',
            old_name='Oil_Viscosity_15C_cp',
            new_name='oil_viscosity_15c_cp',
        ),
        migrations.RenameField(
            model_name='casestudies',
            old_name='Oil_Viscosity_Tr_cp',
            new_name='oil_viscosity_tr_cp',
        ),
    ]
