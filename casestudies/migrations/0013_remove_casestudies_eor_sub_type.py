# Generated by Django 3.2.8 on 2022-08-11 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0012_alter_eortechniques_eor_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudies',
            name='EOR_Sub_Type',
        ),
    ]
