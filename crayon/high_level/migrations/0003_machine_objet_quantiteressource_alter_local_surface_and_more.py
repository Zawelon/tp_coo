# Generated by Django 5.1.1 on 2024-09-25 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0002_local_alter_ville_code_postal_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Machine",
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
                ("prix", models.DecimalField(decimal_places=2, max_digits=10)),
                ("n_serie", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Objet",
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
                ("prix", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="QuantiteRessource",
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
                ("quantite", models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name="local",
            name="surface",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="ville",
            name="prix_par_m2",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name="Etape",
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
                ("duree", models.IntegerField()),
                (
                    "etape_suivante",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="precedente",
                        to="high_level.etape",
                    ),
                ),
                (
                    "machine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.machine",
                    ),
                ),
                (
                    "quantite_ressource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.quantiteressource",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ressource",
            fields=[
                (
                    "objet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="high_level.objet",
                    ),
                ),
            ],
            bases=("high_level.objet",),
        ),
        migrations.CreateModel(
            name="Produit",
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
                (
                    "premiere_etape",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.etape",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("nombre", models.IntegerField()),
                (
                    "objet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.objet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usine",
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
                ("machines", models.ManyToManyField(to="high_level.machine")),
            ],
        ),
        migrations.AddField(
            model_name="quantiteressource",
            name="ressource",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="high_level.ressource"
            ),
        ),
    ]