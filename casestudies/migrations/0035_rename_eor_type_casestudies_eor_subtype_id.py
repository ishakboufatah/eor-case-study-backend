# Generated by Django 3.2.8 on 2022-08-13 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0034_rename_casestudies_id_casestudies_casestudies_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudies',
            old_name='eor_type',
            new_name='eor_subtype_id',
        ),
    ]
