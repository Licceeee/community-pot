"""
Module: course urls

This module defines the URL patterns for the course app.
"""

from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    LearnCraftCourseListView,
    LearnCraftCourseDetailView,
    LearnCraftChapterDetailView,
)

urlpatterns = [
    path(
        "learncraft-courses/",
        login_required(LearnCraftCourseListView.as_view()),
        name="learncraft-course-list",
    ),
    path(
        "learncraft-courses/<int:pk>/chapters/",
        login_required(LearnCraftCourseDetailView.as_view()),
        name="learncraft-course-details",
    ),
    path(
        "learncraft-courses/<int:course>/chapters/<int:pk>",
        login_required(LearnCraftChapterDetailView.as_view()),
        name="learncraft-chapter-details",
    ),
    path("ckeditor/", include("django_ckeditor_5.urls")),
]
