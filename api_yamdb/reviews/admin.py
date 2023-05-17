from django.contrib import admin

from .models import Category, Genre, Comment, Title, GenreTitle, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка Категорий."""

    list_display = (
        'pk',
        'name',
        'slug'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Настройка Жанров."""

    list_display = (
        'pk',
        'name',
        'slug'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GenreTitle)
class GenreTitle(admin.ModelAdmin):
    """Вспомогательная таблица."""

    list_display = (
        'pk',
        'title_id',
        'genre_id'
    )


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Настройка Произведений."""

    list_display = (
        'pk',
        'name',
        'year',
        'description',
    )
    list_filter = ('name',)
    search_fields = ('name', 'year')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка Ревью."""

    list_display = (
        'title',
        'author',
        'text'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка Комментов."""

    list_display = (
        'review',
        'author',
        'text'
    )
