# Generated by Django 3.2.18 on 2023-05-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
