"""
Module: course admin

This module contains the admin classes for the course app.
"""

from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from course.models import Category, Course, Teacher, Lesson, CourseDoc


# ================================================================== >> INLINES
class LessonInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    """Inline class for the Lesson model."""

    model = Lesson
    extra = 1


class CourseDocInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    """Inline class for the CourseDoc model."""

    model = CourseDoc
    extra = 1


@admin.register(Course)
class CourseAdmin(SortableAdminBase, admin.ModelAdmin):
    """Admin class for the Course model."""

    inlines = [LessonInlineAdmin, CourseDocInlineAdmin]
    search_fields = ["title", "teacher"]
    list_display = (
        "title",
        "teacher",
        "category",
        "count_videos",
        "get_image",
    )
    list_filter = ("title", "teacher")
    autocomplete_fields = ["teacher", "category"]
    readonly_fields = ("created", "updated", "headshot_image")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin class for the Category model."""

    search_fields = ["name"]
    list_display = (
        "name",
        "description",
        "online",
        "count_courses",
        "created",
        "updated",
    )
    list_editable = ("online",)
    readonly_fields = ("created", "updated")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Admin class for the Teacher model."""

    search_fields = ["name"]
    list_display = ("name", "created", "updated")
    list_filter = ("name",)
    readonly_fields = ("created", "updated")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Admin class for the Lesson model."""

    search_fields = ["title"]
    list_display = ("title", "course", "day", "created", "updated")
    list_filter = ("course",)
    autocomplete_fields = ["course"]
    readonly_fields = ("created", "updated")


@admin.register(CourseDoc)
class CourseDocAdmin(admin.ModelAdmin):
    """Admin class for the CourseDoc model."""

    search_fields = ["title"]
    list_display = ("title", "course", "created", "updated")
    list_filter = ("course",)
    autocomplete_fields = ["course"]
    readonly_fields = ("created", "updated")
