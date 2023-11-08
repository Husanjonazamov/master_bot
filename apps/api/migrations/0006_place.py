# Generated by Django 4.2.5 on 2023-11-03 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_location_lat_alter_location_lon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('day', models.IntegerField()),
                ('product_count', models.IntegerField()),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='api.location')),
            ],
        ),
    ]