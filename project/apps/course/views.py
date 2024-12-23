"""
Module: course views

This module defines the views for the course app.
"""

from django.views.generic import ListView, DetailView, TemplateView

from course.models import Category, Course


class CategoryListView(ListView):
    """List view for the Category model"""

    template_name = "course/category-list.html"
    model = Category

    def get_context_data(self, **kwargs):
        """The context data for the category list view"""
        context = super().get_context_data(**kwargs)
        context["object_list"] = Category.objects.filter(online=True)
        return context


class CourseListView(TemplateView):
    """List view for the Course model"""

    template_name = "course/course-list.html"
    model = Course

    def get_context_data(self, **kwargs):
        """Returns the context data for the course list view"""
        context = super().get_context_data(**kwargs)

        def get_category_id_from_params():
            """Return category_id from URL params"""
            try:
                return self.kwargs["category_id"]
            except Exception:
                return None

        def get_category_infos():
            """Return title, description, courses of category"""
            category_id = get_category_id_from_params()
            if category_id:
                try:
                    category = Category.objects.get(id=category_id)
                    return (
                        category.name,
                        category.description,
                        Course.objects.filter(category=category_id),
                    )
                except Exception:
                    pass
            return (
                "All courses",
                f"Browse through {Course.objects.count()} courses",
                Course.objects.all(),
            )

        context["title"] = get_category_infos()[0]
        context["description"] = get_category_infos()[1]
        context["courses"] = get_category_infos()[2]
        context["sorted_by_category"] = get_category_id_from_params()
        return context


class CourseDetailView(DetailView):
    """Detail view for the Course model"""

    template_name = "course/course-detail.html"
    model = Course

    def get_context_data(self, **kwargs):
        """Returns the context data for the course detail view"""
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context["title"] = "Course Overview"
        context["nr_lessons"] = self.object.count_videos
        # SEO
        context["page_title"] = "Course Overview"
        context["page_description"] = "Overview of the course"
        return context
