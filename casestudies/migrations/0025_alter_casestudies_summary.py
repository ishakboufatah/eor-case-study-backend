# Generated by Django 3.2.8 on 2022-08-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0024_alter_casestudies_flood_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudies',
            name='summary',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
