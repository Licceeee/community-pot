"""
Module: course views

This module defines the views for the course app.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Course


class LearnCarftView(LoginRequiredMixin, TemplateView):
    """The view for the course list"""

    template_name = "learncraft/course-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ajooooo IRONHACK"
        context["courses"] = Course.objects.all()
        return context
