# Generated by Django 3.2.13 on 2022-05-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='requirement_am',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='requirement',
            name='requirement_or',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='requirement',
            name='requirement_tg',
            field=models.CharField(default='', max_length=255),
        ),
    ]