# Generated by Django 3.1.3 on 2020-11-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_donar_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='checku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=29)),
                ('lname', models.CharField(max_length=29)),
            ],
        ),
    ]