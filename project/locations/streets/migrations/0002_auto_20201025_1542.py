# Generated by Django 3.1.2 on 2020-10-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='street',
            options={'ordering': ('name',)},
        ),
    ]