# Generated by Django 3.2.9 on 2021-11-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_rename_curso_alumnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='No_control',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]