# menu/templatetags/menu_tags.py
from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    menu_tree = build_menu_tree(items, current_url)
    return menu_tree

def build_menu_tree(items, current_url, parent=None):
    menu_tree = []
    for item in items:
        if item.parent == parent:
            children = build_menu_tree(items, current_url, item)
            menu_tree.append({
                'item': item,
                'children': children,
            })
    return menu_tree

