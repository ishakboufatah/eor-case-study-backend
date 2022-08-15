# Generated by Django 3.2.8 on 2022-08-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0035_rename_eor_type_casestudies_eor_subtype_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinCaseStudies',
            fields=[
                ('joincasestudies_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=50)),
                ('eor_type', models.CharField(max_length=50)),
                ('eor_sub_type', models.CharField(max_length=50)),
            ],
        ),
    ]