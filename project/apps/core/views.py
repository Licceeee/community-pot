"""
Module: core views

This module defines the views for the core app.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render


def bad_request(request, exception):
    """Handle 400 errors."""
    return render(request, "core/errors/400.html", status=400)


def permission_denied(request, exception):
    """Handle 403 errors."""
    return render(request, "core/errors/403.html", status=403)


def page_not_found(request, exception):
    """Handle 404 errors."""
    return render(request, "core/errors/404.html", status=404)


def server_error(request):
    """Handle 500 errors."""
    return render(request, "core/errors/500.html", status=500)


def entity_too_large(request):
    """Handle 413 errors."""
    return render(request, "core/errors/413.html", status=413)


class IndexView(LoginRequiredMixin, TemplateView):
    """The view for the index page"""

    template_name = "core/index.html"
