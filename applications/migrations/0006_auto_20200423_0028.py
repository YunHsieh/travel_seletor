# Generated by Django 3.0.2 on 2020-04-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20200423_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=10),
        ),
    ]