# Generated by Django 3.1.1 on 2020-10-06 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Landlord', '0006_merge_20201006_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
