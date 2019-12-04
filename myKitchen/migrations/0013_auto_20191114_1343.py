# Generated by Django 2.2.7 on 2019-11-14 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myKitchen', '0012_auto_20191114_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='materials',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myKitchen.Locations'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='material_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myKitchen.Material_Groups'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='qunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myKitchen.Quantity_Units'),
        ),
        migrations.AlterField(
            model_name='qunits_conversions',
            name='target_qunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myKitchen.Quantity_Units'),
        ),
    ]
