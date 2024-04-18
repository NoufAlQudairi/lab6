# Generated by Django 5.0.4 on 2024-04-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gpa',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
