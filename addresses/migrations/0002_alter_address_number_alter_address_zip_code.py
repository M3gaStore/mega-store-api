# Generated by Django 4.2.2 on 2023-07-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(),
        ),
    ]