# Generated by Django 3.1.2 on 2020-10-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_auto_20201025_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('name',)},
        ),
    ]