# Generated by Django 4.0 on 2023-06-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id', models.CharField(max_length=50, null=True)),
                ('address', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]