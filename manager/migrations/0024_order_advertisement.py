# Generated by Django 2.2 on 2019-05-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0023_auto_20190504_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='advertisement',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
