# Generated by Django 5.0 on 2024-04-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=255)),
                ('Price', models.FloatField()),
                ('Quantity', models.PositiveIntegerField()),
                ('In_stock', models.BooleanField()),
            ],
        ),
    ]
