# Generated by Django 4.2.2 on 2023-07-03 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='products.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_cart',
            field=models.ManyToManyField(related_name='cart_products', through='carts.CartItem', to='products.product'),
        ),
    ]
