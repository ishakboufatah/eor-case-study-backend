# Generated by Django 3.2.8 on 2022-08-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0011_auto_20220811_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eortechniques',
            name='EOR_Type',
            field=models.CharField(max_length=100),
        ),
    ]
