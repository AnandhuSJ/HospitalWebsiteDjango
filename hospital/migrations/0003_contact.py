# Generated by Django 3.2.9 on 2021-12-05 16:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_sub_e_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('deid', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('subject', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('message', models.CharField(max_length=800)),
            ],
        ),
    ]
