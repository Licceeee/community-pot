"""
Module: course models

This module contains the models for the course app.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_ckeditor_5.fields import CKEditor5Field


class Course(models.Model):
    """Model for a course."""

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("Title of the course."),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Description of the course."),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
        help_text=_("Date and time when the course was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
        help_text=_("Date and time when the course was last updated."),
    )

    def __str__(self):
        """Returns the string representation of the course."""
        return self.title


class Chapter(models.Model):
    """Model for a chapter."""

    course = models.ForeignKey(
        Course,
        related_name="chapters",
        on_delete=models.CASCADE,
        verbose_name=_("Course"),
        help_text=_("Course to which the chapter belongs."),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("Title of the chapter."),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
        help_text=_("Date and time when the chapter was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
        help_text=_("Date and time when the chapter was last updated."),
    )
    chapter_nr = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Chapter number"),
        help_text=_("Number of the chapter."),
    )

    class Meta:
        """Meta options for the course model."""

        # Ensure chapter numbers are unique within a course
        unique_together = (
            "course",
            "chapter_nr",
        )

    def __str__(self):
        """Returns the string representation of the chapter."""
        return f"{self.title} - {self.course.title}"


class Section(models.Model):
    """Model for a section."""

    chapter = models.ForeignKey(
        Chapter,
        related_name="sections",
        on_delete=models.CASCADE,
        verbose_name=_("Chapter"),
        help_text=_("Chapter to which the section belongs."),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("Title of the section."),
    )
    section_nr = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Section number"),
        help_text=_("Number of the section."),
    )
    content = CKEditor5Field("Content", config_name="extends")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
        help_text=_("Date and time when the section was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
        help_text=_("Date and time when the section was last updated."),
    )

    class Meta:
        """Meta options for the section model."""

        # Ensure section numbers are unique within a chapter
        unique_together = (
            "chapter",
            "section_nr",
        )

    def __str__(self):
        """Returns the string representation of the section."""
        return f"{self.title} - {self.chapter.title}"


class VideoUpload(models.Model):
    """Model for video uploads associated with a chapter."""

    chapter = models.ForeignKey(
        Chapter,
        related_name="videos",
        on_delete=models.CASCADE,
        verbose_name=_("Chapter"),
        help_text=_("Chapter to which the video belongs."),
    )
    video = models.FileField(
        upload_to="videos/",
        verbose_name=_("Video"),
        help_text=_("Uploaded video file."),
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Uploaded at"),
        help_text=_("Date and time when the video was uploaded."),
    )

    def __str__(self):
        """Returns the string representation of the video upload."""
        return f"Video for {self.chapter.title}"
