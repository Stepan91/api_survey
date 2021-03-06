# Generated by Django 2.2.10 on 2021-04-20 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_start', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата начала')),
                ('date_finish', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата окончания')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type_question', models.CharField(choices=[('text', 'ответ текстом'), ('single_value', 'ответ с выбором одного значения'), ('multi_value', 'ответ с выбором нескольких вариантов')], max_length=11)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.Survey')),
            ],
        ),
    ]
