from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from core.constants import BASE_URL, HOST
from menus.models import Menu, MenuItem


def menus(request: HttpRequest) -> HttpResponse:
    """Обработка перехода на главную страницу.

    Args:
        request: Передаваемый запрос.

    Returns:
        Рендер главной страницы.
    """
    current_url = HOST + request.path
    if current_url != BASE_URL + '/':
        try:
            get_object_or_404(MenuItem, url=current_url)
        except Http404:
            get_object_or_404(Menu, url=current_url)
    return render(
        request,
        'menus/menus.html',
        {'menus': Menu.objects.all(), 'current_url': current_url},
    )
