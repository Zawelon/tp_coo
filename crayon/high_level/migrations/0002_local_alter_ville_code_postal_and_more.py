# Generated by Django 5.1.1 on 2024-09-25 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Local",
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
                ("nom", models.CharField(max_length=100)),
                ("surface", models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name="ville",
            name="code_postal",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="ville",
            name="prix_par_m2",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="SiegeSocial",
            fields=[
                (
                    "local_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="high_level.local",
                    ),
                ),
            ],
            bases=("high_level.local",),
        ),
        migrations.AddField(
            model_name="local",
            name="ville",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="high_level.ville"
            ),
        ),
    ]
