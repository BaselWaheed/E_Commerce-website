# Generated by Django 3.1.5 on 2022-08-27 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220827_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.size', verbose_name='size'),
        ),
    ]
