# Generated by Django 4.2.5 on 2023-09-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_delivered_options_alter_veterinarian_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
