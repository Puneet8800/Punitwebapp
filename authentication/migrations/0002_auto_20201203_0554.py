# Generated by Django 3.1.3 on 2020-12-03 05:54

from django.db import migrations
import mirage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='ssn',
            field=mirage.fields.EncryptedIntegerField(max_length=64),
        ),
    ]
