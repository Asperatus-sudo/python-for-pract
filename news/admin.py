from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "created_at",
        "is_published",
        "author",
    )

    list_filter = (
        "is_published",
        "created_at",
        "category",
        "id",
        "title",
        "author",
    )

    search_fields = (
        "title",
        "content",
        "author",
        "created_at",
    )

    ordering = (
        "-created_at",
    )
# Register your models here.
