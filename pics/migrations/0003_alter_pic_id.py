# Generated by Django 4.0.6 on 2024-02-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_auto_20200321_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]