# Generated by Django 5.0 on 2023-12-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_cart_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstcart',
            name='product_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
