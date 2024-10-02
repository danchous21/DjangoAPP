from django.shortcuts import render

from .models import MenuItem


def build_menu_tree(items, parent=None):
    """
    Рекурсивно строим дерево меню из элементов MenuItem.
    """
    menu_tree = []
    for item in items:
        if item.parent == parent:
            item.children_list = build_menu_tree(items, item)
            menu_tree.append(item)
    return menu_tree


def services_view(request):
    """
    Отображение страницы услуг.
    """
    return render(request, 'services.html')


def about_view(request):
    """
    Отображение страницы о нас.
    """
    return render(request, 'about.html')


def web_development_view(request):
    """
    Отображение страницы веб-разработки.
    """
    return render(request, 'services/web_development.html')


def mobile_development_view(request):
    """
    Отображение страницы мобильной разработки.
    """
    return render(request, 'services/mobile_development.html')


def menu_view(request):
    """
    Отображение страницы меню.
    """
    menu_items = MenuItem.objects.all()
    menu_tree = build_menu_tree(menu_items)
    return render(request, 'menu/menu.html', {'menu_tree': menu_tree})
