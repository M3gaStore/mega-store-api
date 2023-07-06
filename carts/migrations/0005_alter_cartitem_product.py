# Generated by Django 4.2.2 on 2023-07-06 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_is_available_alter_product_quantity_in_stock_and_more'),
        ('carts', '0004_alter_cart_product_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
