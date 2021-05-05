from django.contrib import admin
from .models import kurser, books, plakater, om, about


@admin.register(kurser)
class kurseradmin(admin.ModelAdmin):
    list_display = ("titel", "slug", "billede")


@admin.register(om)
class OMadmin(admin.ModelAdmin):
    list_display = ("titel", "slug", "billede")


@admin.register(about)
class aboutadmin(admin.ModelAdmin):
    list_display = ("tekst",)


@admin.register(books)
class booksadmin(admin.ModelAdmin):
    list_display = ("titel", "tekst", "billede")


@admin.register(plakater)
class plakateradmin(admin.ModelAdmin):
    list_display = ("titel", "billede")
