# Generated by Django 2.2 on 2019-05-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_expenditure_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ship_to',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_to_address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_to_company_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_to_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_handling',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_rate',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_tax',
            field=models.IntegerField(default=0),
        ),
    ]