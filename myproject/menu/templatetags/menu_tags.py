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
    tree = []
    for item in items.filter(parent=parent):
        item.is_active = current_url == item.url or (item.named_url and request.resolver_match.url_name == item.named_url)
        item.children = build_menu_tree(items, current_url, item)
        tree.append(item)
    return tree
