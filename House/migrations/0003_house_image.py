# Generated by Django 3.1.1 on 2020-09-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0002_auto_20200923_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='images/th.jpg', null=True, upload_to='images/Houes'),
        ),
    ]
