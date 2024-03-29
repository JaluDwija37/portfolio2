# Generated by Django 4.2.7 on 2023-11-16 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("programing_language", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkillModel",
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
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("pemula", "Pemula"),
                            ("menengah", "Menengah"),
                            ("mahir", "Mahir"),
                            ("ahli", "Ahli"),
                        ],
                        default="pemula",
                        max_length=50,
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="programing_language.proglangmodel",
                    ),
                ),
            ],
        ),
    ]
