# Generated by Django 4.0.3 on 2024-01-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Author', models.CharField(max_length=255)),
                ('ISBN', models.IntegerField()),
            ],
        ),
    ]
