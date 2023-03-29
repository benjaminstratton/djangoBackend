# Generated by Django 4.1.7 on 2023-03-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('astronomer', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('coordinates', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
