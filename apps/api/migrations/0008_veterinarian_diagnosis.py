# Generated by Django 4.2.5 on 2023-11-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_place_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinarian',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
    ]