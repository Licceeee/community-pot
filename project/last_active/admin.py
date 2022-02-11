from django.contrib import admin

# Register your models here.
from .models import LastActive


class LastActiveAdmin(admin.ModelAdmin):
    list_filter = ("site", "module", "last_active")
    search_fields = ("user__username",)
    list_display = ("site", "module", "user", "last_active")
    readonly_fields = ['last_active', 'user', 'site', 'module']


admin.site.register(LastActive, LastActiveAdmin)
