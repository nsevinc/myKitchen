# Generated by Django 2.2.7 on 2019-11-14 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myKitchen', '0005_auto_20191114_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materials',
            old_name='qunit',
            new_name='qunit_id',
        ),
    ]
