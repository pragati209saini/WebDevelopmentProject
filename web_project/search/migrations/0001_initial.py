# Generated by Django 3.1.3 on 2020-12-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('logo_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
