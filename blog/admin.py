from django.contrib import admin
from .models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # выводит атрибуты
    list_filter = ('status', 'created', 'publish', 'author')
    # добавляет фильтр по атрибутам

    search_fields = ('title', 'body')
    # Поисковая строка по body и title

    prepopulated_fields = {'slug': ('title',)}
    # вставляет на место slug -< title

    raw_id_fields = ('author',)
    # улучшенный список авторов

    date_hierarchy = 'publish'
    # добовляет иерархию по времени создания

    ordering = ('status', 'publish')
    # сортировка
    pass
# Register your models here.
