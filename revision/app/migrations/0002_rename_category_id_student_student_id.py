# Generated by Django 4.0 on 2023-06-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='category_id',
            new_name='student_id',
        ),
    ]
