from django.contrib import admin
from .models import Movie, Director, Genre, Actor
from django.contrib.auth.models import User
from django.utils.html import format_html


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genre', 'cast',)
    list_display = ('title', 'directed_by', 'display_genre', 'display_cast_pink', 'date_released',)
    list_display_links = ('title',)
    list_editable = ('directed_by', 'date_released')
    list_filter = ('genre',)
    list_per_page = 10


    def display_cast_pink(self, obj):
        """Create a bold pink string for the Actors. This is required to display cast in Admin."""
        self.collect_cast = ', '.join(f'{actor.first_name} {actor.last_name}' for actor in obj.cast.all()),

        return format_html(
            '<span style="color: #FF69B4;">{}</span>',
            self.collect_cast,
        )
    display_cast_pink.short_description = "Cast"
    empty_value_display = "None"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'),)

admin.site.register(Director)
admin.site.register(Genre)