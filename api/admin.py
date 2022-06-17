from django.contrib import admin

# Register your models here.

from .models import Note

@admin.site.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'updated', 'created')
    list_filter = ('updated', 'created')
    search_fields = ('body',)
