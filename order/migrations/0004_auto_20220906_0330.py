# Generated by Django 3.1.5 on 2022-09-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='size'),
        ),
    ]