# Generated by Django 3.1.5 on 2022-08-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220826_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_added',
            field=models.DateField(auto_now=True, verbose_name='added time'),
        ),
    ]
