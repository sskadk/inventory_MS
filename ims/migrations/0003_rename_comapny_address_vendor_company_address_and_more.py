# Generated by Django 5.2.3 on 2025-06-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0002_customer_department_producttype_purchase_sell_vendor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='comapny_address',
            new_name='company_address',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(blank=True, to='ims.department'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sell',
            name='price',
            field=models.FloatField(),
        ),
    ]
