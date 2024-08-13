# Generated by Django 5.0.7 on 2024-07-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examPortal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('class1', models.CharField(choices=[('1', '10th'), ('2', '12th'), ('3', 'UG'), ('4', 'PG')], max_length=1)),
                ('email', models.CharField(max_length=55)),
                ('mobNo', models.CharField(max_length=13, verbose_name=int)),
                ('age', models.CharField(max_length=3, verbose_name=int)),
            ],
        ),
    ]
