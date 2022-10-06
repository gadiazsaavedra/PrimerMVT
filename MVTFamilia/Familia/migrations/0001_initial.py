# Generated by Django 4.1.1 on 2022-10-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Familia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30)),
                ("edad", models.IntegerField()),
                ("rol", models.CharField(max_length=30)),
                ("profesion", models.CharField(max_length=30)),
                ("fecha_nacimiento", models.DateField()),
            ],
        ),
    ]
