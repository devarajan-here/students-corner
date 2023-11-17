# Generated by Django 4.1.4 on 2023-06-23 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("roll_no", models.PositiveIntegerField()),
                ("parrent_phno", models.PositiveIntegerField()),
                ("whatsno", models.IntegerField()),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("cse", "Computer Engineering"),
                            ("eee", "Eletrical Engineering"),
                            ("civil", "Civil Engineering"),
                            ("mech", "Mechanical Engineering"),
                            ("ice", "Instrumental Engineering"),
                        ],
                        default="cse",
                        max_length=5,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["roll_no"],
            },
        ),
    ]
