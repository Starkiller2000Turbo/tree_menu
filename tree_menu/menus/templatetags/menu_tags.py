from typing import Any, Dict

from django import template

from menus.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menus/menu.html', takes_context=True)
def draw_menu(context: Dict[str, Any], menu: Menu) -> Dict[str, Any]:
    """Тег для отображения меню.

    Args:
        menu: меню, которое необходимо отобразить.

    Returns:
        Словарь, содержащий имя меню и корневой элемень.
    """
    current_url = context.get('current_url')
    return {
        'name': menu.name,
        'root_item': menu.root_item,
        'url': menu.url,
        'current_url': current_url,
    }


@register.inclusion_tag('menus/menu_item.html', takes_context=True)
def draw_menu_item(context: Dict[str, Any], item: MenuItem) -> Dict[str, Any]:
    """Тег для отображения элемента меню.

    Args:
        item: элемент меню, который необходимо отобразить.

    Returns:
        Словарь с именем, уровнем элемента и дочерними элементами.
    """
    current_url = context.get('current_url')
    return {
        'name': item.name,
        'level': item.level,
        'children': item.children.all(),
        'url': item.url,
        'current_url': current_url,
    }
