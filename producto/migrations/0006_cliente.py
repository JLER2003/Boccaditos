# Generated by Django 4.2.2 on 2023-06-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField(blank=True)),
            ],
        ),
    ]