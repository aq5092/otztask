# Generated by Django 5.1.4 on 2025-01-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='javobgar',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
