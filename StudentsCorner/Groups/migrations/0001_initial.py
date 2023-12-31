# Generated by Django 4.1.4 on 2023-06-23 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Student", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AttendanceStatus",
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
                ("is_present", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=40)),
                ("slug", models.SlugField(allow_unicode=True, unique=True)),
                (
                    "for_class",
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
                ("class_start_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="GroupMembers",
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
                ("join_date", models.DateField(auto_now_add=True)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="membership",
                        to="Groups.group",
                    ),
                ),
                (
                    "students",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_groups",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("group", "students")},
            },
        ),
        migrations.AddField(
            model_name="group",
            name="students",
            field=models.ManyToManyField(
                through="Groups.GroupMembers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Attendence",
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
                ("date", models.DateField()),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Groups.group"
                    ),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        through="Groups.AttendanceStatus", to="Student.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="attendancestatus",
            name="attendance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Groups.attendence"
            ),
        ),
        migrations.AddField(
            model_name="attendancestatus",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Student.student"
            ),
        ),
    ]
