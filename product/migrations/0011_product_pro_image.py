# Generated by Django 3.1.5 on 2022-08-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20220827_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_image',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='image'),
        ),
    ]
