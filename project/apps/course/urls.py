"""
Module: course urls

This module defines the URL patterns for the course app.
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CategoryListView, CourseListView, CourseDetailView


urlpatterns = [
    path("", login_required(CategoryListView.as_view()), name="category-list"),
    path(
        "<int:category_id>/courses",
        login_required(CourseListView.as_view()),
        name="course-list",
    ),
    path(
        "courses/",
        login_required(CourseListView.as_view()),
        name="course-list",
    ),
    path(
        "courses/<int:pk>",
        login_required(CourseDetailView.as_view()),
        name="course-detail",
    ),
]
