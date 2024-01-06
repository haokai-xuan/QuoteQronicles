from django.contrib import admin
from .models import Author, Quote

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote', 'author', 'date_created')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)