# Generated by Django 3.2.8 on 2022-08-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0017_alter_image_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image1',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
