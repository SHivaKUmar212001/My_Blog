# Generated by Django 3.2.6 on 2021-08-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_auto_20210811_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]