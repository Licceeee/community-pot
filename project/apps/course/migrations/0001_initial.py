# Generated by Django 5.1.2 on 2024-10-21 12:46

import course.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(null=True)),
                (
                    "icon_source",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("online", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
            },
        ),
        migrations.CreateModel(
            name="Course",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "folder_name",
                    models.CharField(max_length=100, null=True, unique=True),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=course.models.img_upload_path
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.category",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.teacher",
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="CourseDoc",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("sortable_inline_order", models.PositiveIntegerField(default=0)),
                ("day", models.IntegerField(blank=True, null=True)),
                (
                    "file",
                    models.FileField(
                        blank=True, default=None, null=True, upload_to="uploads/"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Course Doc",
                "verbose_name_plural": "Course Docs",
                "ordering": ["sortable_inline_order"],
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("day", models.IntegerField(blank=True, null=True)),
                ("sortable_inline_order", models.PositiveIntegerField(default=0)),
                ("url", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "course",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lesson",
                "ordering": ["sortable_inline_order"],
            },
        ),
    ]
