# Generated by Django 3.2.8 on 2021-11-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
