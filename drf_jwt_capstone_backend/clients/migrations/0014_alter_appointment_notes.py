# Generated by Django 3.2.8 on 2022-01-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_appointment_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
