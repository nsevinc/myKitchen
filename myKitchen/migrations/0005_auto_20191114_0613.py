# Generated by Django 2.2.7 on 2019-11-14 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myKitchen', '0004_auto_20191113_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='stocktype',
        ),
        migrations.AddField(
            model_name='materials',
            name='qunit',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myKitchen.quantity_units'),
            preserve_default=False,
        ),
    ]
