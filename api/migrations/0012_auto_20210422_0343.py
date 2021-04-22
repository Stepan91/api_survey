# Generated by Django 2.2.10 on 2021-04-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210422_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='date_finish',
            field=models.DateTimeField(db_index=True, verbose_name='date_finish'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date_start'),
        ),
    ]
