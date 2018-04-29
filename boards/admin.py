from django.contrib import admin

from . import models


@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "comment",
        "get_style_display",
        "latitude",
        "longitude",
        "get_artery_display",
        "status",
        "prepared_by",
    )
