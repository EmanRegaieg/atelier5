from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation', 'publie')
    list_filter = ('publie',)
    search_fields = ('titre', 'auteur')