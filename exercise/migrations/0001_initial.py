# Generated by Django 5.2 on 2025-04-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('flexibility', 'Flexibility'), ('balance', 'Balance')], default='cardio', max_length=20)),
                ('calories_burned_per_hour', models.PositiveIntegerField()),
            ],
        ),
    ]
