# Generated by Django 3.2.13 on 2022-04-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options'),
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotelineitem',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.quotearea'),
        ),
        migrations.AlterField(
            model_name='quotelineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
