# Generated by Django 3.1.3 on 2020-12-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20201202_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
