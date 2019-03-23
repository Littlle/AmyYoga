# Generated by Django 2.1.7 on 2019-03-23 15:52

import Interface.Interface
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('authoritySignal', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, Interface.Interface.CustomerInterface),
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phoneNumber', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('birthday', models.DateField(default='1970-01-01')),
                ('profession', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=False)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('bust', models.FloatField(default=0)),
                ('waistline', models.FloatField(default=0)),
                ('hipline', models.FloatField(default=0)),
                ('shoulderwidth', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, Interface.Interface.PersonalInformationInterface),
        ),
    ]
