"""
Module: learncraft admin

This module contains the admin classes for the learncraft app.
"""

from django.contrib import admin

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from .models import Course, Chapter, Section, VideoUpload


class VideoUploadInline(admin.StackedInline):
    """Inline class for the VideoUpload model."""

    model = VideoUpload
    extra = 0


class ChapterInline(SortableInlineAdminMixin, admin.StackedInline):
    """Inline class for the Chapter model."""

    model = Chapter
    extra = 0


class SectionInline(SortableInlineAdminMixin, admin.StackedInline):
    """Inline class for the Section model."""

    model = Section
    extra = 0


@admin.register(Course)
class CourseAdmin(SortableAdminBase, admin.ModelAdmin):
    """Admin class for the Course model."""

    inlines = [ChapterInline]
    list_display = ("title", "get_nr_chapters", "created_at")
    search_fields = ("title",)


@admin.register(Chapter)
class ChapterAdmin(SortableAdminBase, admin.ModelAdmin):
    """Admin class for the Chapter model."""

    inlines = [VideoUploadInline, SectionInline]
    list_display = (
        "title",
        "chapter_nr",
        "course",
        "get_nr_sections",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)
    list_filter = ("course",)

    def save_model(self, request, obj, form, change):
        """Override save_model to block non-superusers from saving."""
        if not request.user.is_superuser:
            return  # Prevent saving the object
        super().save_model(request, obj, form, change)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """Admin class for the Section model."""

    list_display = (
        "title",
        "section_nr",
        "chapter",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "chapter__title")
    autocomplete_fields = ("chapter",)
    list_filter = ("chapter",)

    def save_model(self, request, obj, form, change):
        """Override save_model to block non-superusers from saving."""
        if not request.user.is_superuser:
            return  # Prevent saving the object
        super().save_model(request, obj, form, change)
