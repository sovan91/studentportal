# Generated by Django 3.1.1 on 2020-09-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200912_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Mob',
            field=models.CharField(max_length=20),
        ),
    ]
