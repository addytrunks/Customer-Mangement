# Generated by Django 3.0 on 2020-07-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_auto_20200711_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]