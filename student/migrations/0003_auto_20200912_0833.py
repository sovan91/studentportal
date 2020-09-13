# Generated by Django 3.1.1 on 2020-09-12 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200911_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.IntegerField()),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Mob', models.IntegerField()),
                ('Add', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentRegistration',
        ),
    ]