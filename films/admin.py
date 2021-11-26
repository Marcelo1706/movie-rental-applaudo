from django.contrib import admin

from .models import Kind, Film, Role, Person, FilmPerson, Season, Episode


class KindAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('given_name', 'last_name', 'created_at', 'updated_at')
    search_fields = ('given_name', 'last_name')
    ordering = ('given_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at')


class FilmPersonAdmin(admin.ModelAdmin):
    list_display = ('person', 'film', 'role', 'created_at', 'updated_at')
    search_fields = ('film__title',
                     'person__given_name',
                     'person__last_name',
                     'role__name')
    ordering = ('person', 'film', 'role')
    readonly_fields = ('created_at', 'updated_at')


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'film', 'created_at', 'updated_at')
    search_fields = ('name', 'film__title')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'created_at', 'updated_at')
    search_fields = ('name', 'season__name')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


# Register your models here.
admin.site.register(Kind, KindAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(FilmPerson, FilmPersonAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)
