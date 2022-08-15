# Generated by Django 3.2.8 on 2022-08-13 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0032_alter_casestudies_eor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudies',
            name='eor_type',
            field=models.ForeignKey(blank=True, db_column='eor_subtype_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casestudies.eorsubtype'),
        ),
        migrations.AlterField(
            model_name='eorsubtype',
            name='eor_type',
            field=models.ForeignKey(db_column='eor_techniques_id', on_delete=django.db.models.deletion.DO_NOTHING, to='casestudies.eortechniques'),
        ),
    ]