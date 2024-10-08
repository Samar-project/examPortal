# Generated by Django 5.0.7 on 2024-08-10 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examPortal', '0003_alter_userregistration_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userregistration',
            options={},
        ),
        migrations.AlterModelManagers(
            name='userregistration',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='email1',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='passwd',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='usernm',
        ),
        migrations.AddField(
            model_name='userregistration',
            name='id',
            field=models.BigAutoField(auto_created=True, default=102, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregistration',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
