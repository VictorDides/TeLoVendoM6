# Generated by Django 4.2.3 on 2023-07-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=254)),
            ],
        ),
    ]
