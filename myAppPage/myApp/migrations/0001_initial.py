# Generated by Django 4.2.1 on 2023-06-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=15)),
            ],
        ),
    ]
