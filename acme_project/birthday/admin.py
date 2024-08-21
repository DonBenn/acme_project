from django.contrib import admin  # type: ignore

from .models import Birthday, Tag

admin.site.register(Birthday)
admin.site.register(Tag)
