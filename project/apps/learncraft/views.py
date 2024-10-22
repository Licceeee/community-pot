from django.views.generic import ListView, DetailView, TemplateView
from .models import Course


class LearnCarftView(TemplateView):
    template_name = "learncraft/course-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ajooooo IRONHACK"
        context["courses"] = Course.objects.all()
        return context
