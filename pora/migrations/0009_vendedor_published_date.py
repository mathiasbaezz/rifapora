# Generated by Django 3.2.5 on 2021-08-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pora', '0008_rename_codigo_qr_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
