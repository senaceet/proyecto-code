# Generated by Django 3.2.6 on 2021-09-12 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_rename_estado_productos_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='estado',
            new_name='Estado',
        ),
    ]
