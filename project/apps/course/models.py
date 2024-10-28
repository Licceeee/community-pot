"""
Module: course models

This module contains the models for the course app.
"""

from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Timestamps
from core.libs.core_libs import get_headshot_image, get_image_format


def img_upload_path(instance, filename):
    """Generate a unique path for the uploaded image"""
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = f"{instance.pk}.{ext}"
    else:
        # set filename as random string
        filename = f"{uuid4().hex}.{ext}"
    return f"courses/intro_images/{filename}"


class Category(Timestamps):
    """The Category model represents a course category."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Name"),
        help_text=_("Name of the category."),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Description of the category."),
    )
    icon_source = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Icon Source"),
        help_text=_("Icon source of the category."),
    )
    online = models.BooleanField(default=False)

    class Meta:
        """Meta options for the Category model."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Returns the string representation of the category."""
        return f"{self.name}"

    def count_courses(self):
        """Returns the number of courses in the category"""
        return self.course_set.count()

    count_courses.short_description = "# Courses"


class Teacher(Timestamps):
    """The Teacher model represents a course teacher."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        """Meta options for the Teacher model."""

        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        """Returns the string representation of the teacher."""
        return f"{self.name}"


class Course(Timestamps):
    """The Course model represents a course."""

    category = models.ForeignKey(
        Category,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        help_text=_("Category to which the course belongs."),
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Title"),
        help_text=_("Title of the course."),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Description of the course."),
    )
    teacher = models.ForeignKey(
        Teacher,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Teacher"),
        help_text=_("Teacher of the course."),
    )
    folder_name = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        verbose_name=_("Folder Name"),
        help_text=_("Folder name of the course."),
    )
    image = models.ImageField(
        upload_to=img_upload_path,
        null=True,
        blank=True,
        verbose_name=_("Image"),
        help_text=_("Image of the course."),
    )

    class Meta(object):
        """Meta options for the Course model."""

        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        """Returns the string representation of the course."""
        return f"{self.title}"

    def count_videos(self):
        """Returns the number of videos in the course"""
        return self.lesson_set.count()

    count_videos.short_description = "# Videos"

    def headshot_image(self):
        """Returns the headshot image of the course"""
        return get_headshot_image(self.image, 300)

    headshot_image.short_description = "Preview"

    def get_image(self):
        """Returns the image of the course"""
        if self.image:
            return get_image_format(self.image, 100)
        return "No Image"

    get_image.short_description = "Image"


class Lesson(Timestamps):
    """The Lesson model represents a course lesson."""

    title = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
        help_text=_("Title of the lesson."),
    )
    course = models.ForeignKey(
        Course,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Course"),
        help_text=_("Course to which the lesson belongs."),
    )
    day = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("Day"),
        help_text=_("Day of the lesson."),
    )
    sortable_inline_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("Order"),
        help_text=_("Order of the lesson."),
    )
    url = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("URL"),
        help_text=_("URL of the lesson."),
    )

    class Meta(object):
        """The Meta options for the Lesson model."""

        verbose_name = "Lesson"
        verbose_name_plural = "Lesson"
        ordering = ["sortable_inline_order"]

    def __str__(self):
        """Returns the string representation of the lesson."""
        return f"{self.title}"


class CourseDoc(Timestamps):
    """The CourseDoc model represents a course document."""

    title = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
        help_text=_("Title of the course doc."),
    )
    course = models.ForeignKey(
        Course,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Course"),
        help_text=_("Course to which the course doc belongs."),
    )
    sortable_inline_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=_("Order"),
        help_text=_("Order of the course doc."),
    )
    day = models.IntegerField(null=True, blank=True)
    file = models.FileField(
        default=None,
        upload_to="uploads/",
        null=True,
        blank=True,
        verbose_name=_("File"),
        help_text=_("File of the course doc."),
    )

    class Meta(object):
        """The Meta options for the CourseDoc model"""

        verbose_name = "Course Doc"
        verbose_name_plural = "Course Docs"
        ordering = ["sortable_inline_order"]

    def __str__(self):
        """Returns the string representation of the course doc."""
        return f"{self.title}"
