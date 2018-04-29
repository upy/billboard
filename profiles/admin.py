from django.contrib import admin

from . import models, forms


@admin.register(models.Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "email", "phone", "is_active"
    )
    form = forms.RepresentativeForm
