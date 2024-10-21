from django.contrib import admin

from course.models import Course, Chapter, Section


class SectionInline(admin.StackedInline):
    """Inline class for the Section model."""

    model = Section
    extra = 1


class ChapterInline(admin.StackedInline):
    """Inline class for the Chapter model."""

    model = Chapter
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin class for the Course model."""

    inlines = [ChapterInline]
    list_display = ("title", "created_at")
    search_fields = ("title",)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    """Admin class for the Chapter model."""

    inlines = [SectionInline]
    list_display = (
        "title",
        "chapter_nr",
        "course",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)


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
