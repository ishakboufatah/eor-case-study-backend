# Generated by Django 3.2.8 on 2022-08-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0023_auto_20220812_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudies',
            name='Flood_Type',
            field=models.CharField(blank=True, choices=[('Vertical', 'Vertical'), ('Horizontal', 'Horizontal'), ('Combination', 'Combination')], max_length=15, null=True),
        ),
    ]