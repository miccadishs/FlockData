# Generated by Django 3.1.4 on 2021-03-12 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flocks', '0005_auto_20210312_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='attendent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flocks.farmattendent'),
        ),
    ]
