# Generated by Django 3.2.6 on 2021-09-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20210909_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=2000),
        ),
    ]
