# Generated by Django 3.2.18 on 2023-12-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_bookings_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='restaurant',
            field=models.CharField(choices=[('Tonys', 'Tonys'), ('The Char Grill', 'The Char Grill'), ('Mama Mia', 'Mama mia')], default='Tonys', max_length=100),
        ),
    ]
