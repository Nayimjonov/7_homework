# Generated by Django 5.2 on 2025-04-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('blood_pressure_systolic', models.PositiveIntegerField(blank=True, null=True)),
                ('blood_pressure_diastolic', models.PositiveIntegerField(blank=True, null=True)),
                ('heart_rate', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
