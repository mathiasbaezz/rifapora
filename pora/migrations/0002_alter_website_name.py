# Generated by Django 3.2.5 on 2021-08-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
