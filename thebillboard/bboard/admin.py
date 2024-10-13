from django.contrib import admin

from .models import Objects


class ObjectsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "title",
        "price",
        "time_create",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)


admin.site.register(Objects, ObjectsAdmin)
