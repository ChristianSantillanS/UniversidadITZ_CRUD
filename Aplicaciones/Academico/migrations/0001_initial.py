# Generated by Django 3.2.9 on 2021-11-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('No_control', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellido_p', models.CharField(max_length=30)),
                ('Apellido_m', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=60)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]