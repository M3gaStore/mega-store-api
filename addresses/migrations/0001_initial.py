# Generated by Django 4.2.2 on 2023-07-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('neighborhood', models.CharField(max_length=60)),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]
