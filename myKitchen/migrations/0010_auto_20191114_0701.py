# Generated by Django 2.2.7 on 2019-11-14 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myKitchen', '0009_auto_20191114_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qunits_Conversions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faktor', models.FloatField(default=1)),
                ('target_qunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myKitchen.Quantity_Units')),
            ],
        ),
        migrations.DeleteModel(
            name='malzemeler',
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
    ]
