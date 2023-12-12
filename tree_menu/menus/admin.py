from django.contrib import admin

from core.admin import BaseAdmin
from menus.models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(BaseAdmin):
    """Способ отображения поста в админке."""

    list_display = (
        'name',
        'parent',
        'directory',
        'url',
        'level',
        'menu',
        'is_root',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    readonly_fields = ('url', 'level')
    ordering = ('url',)


class MenuItemInlineAdmin(admin.TabularInline):
    """Представление модели тега в рецепте."""

    model = MenuItem
    readonly_fields = ('url', 'level')
    ordering = ('url',)


@admin.register(Menu)
class MenuAdmin(BaseAdmin):
    """Способ отображения поста в админке."""

    list_display = (
        'name',
        'root_item',
        'url',
    )
    search_fields = ('name',)
    list_filter = ('name', 'root_item')
    readonly_fields = ('url',)
    inlines = [MenuItemInlineAdmin]
