# Generated by Django 4.1.7 on 2023-03-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='type',
            field=models.CharField(choices=[('Bus', 'Bus'), ('Train', 'Train'), ('Plane', 'Plane')], default='Bus', max_length=10),
        ),
    ]
