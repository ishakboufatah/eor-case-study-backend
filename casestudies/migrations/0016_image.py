# Generated by Django 3.2.8 on 2022-08-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0015_alter_casestudies_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMAGE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
