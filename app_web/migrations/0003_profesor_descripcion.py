# Generated by Django 5.1.3 on 2024-12-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0002_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
