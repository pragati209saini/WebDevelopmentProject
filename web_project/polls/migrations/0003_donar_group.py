# Generated by Django 3.1.3 on 2020-11-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201129_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='donar',
            name='group',
            field=models.CharField(max_length=30, null=True),
        ),
    ]