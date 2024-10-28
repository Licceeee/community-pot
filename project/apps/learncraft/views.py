"""
Module: course views

This module defines the views for the course app.
"""

from django.views.generic import ListView, DetailView

from .models import Course, Chapter


class LearnCraftCourseListView(ListView):
    """The view for the learncraft course list."""

    template_name = "learncraft/course-list.html"
    model = Course

    def get_context_data(self, **kwargs):
        """Returns the context data for the course list view."""
        context = super().get_context_data(**kwargs)
        context["object_list"] = Course.objects.all()

        return context


class LearnCraftCourseDetailView(DetailView):
    """The view for the learncraft course list."""

    template_name = "learncraft/chapter-list.html"
    model = Course

    def get_context_data(self, **kwargs):
        """Returns the context data for the course list view."""
        context = super().get_context_data(**kwargs)

        return context


class LearnCraftChapterDetailView(DetailView):
    """The view for the learncraft course list."""

    template_name = "learncraft/section-list.html"
    model = Chapter

    def get_context_data(self, **kwargs):
        """Returns the context data for the course list view."""
        context = super().get_context_data(**kwargs)
        chapter = self.object  # Get the current chapter instance
        next_chapter = chapter.get_next_chapter()  # Get the next chapter
        previous_chapter = chapter.get_previous_chapter()

        context['next_chapter'] = next_chapter
        context['previous_chapter'] = previous_chapter

        return context
