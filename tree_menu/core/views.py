from http import HTTPStatus

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls.exceptions import Resolver404


def page_not_found(
    request: HttpRequest,
    exception: Resolver404,
) -> HttpResponse:
    """Функция для вывода кастомной страницы ошибки 404.

    Args:
        request: передаваемый запрос.
        exception: вызываемое исключение.

    Returns:
        рендер страницы ошибки 404.
    """
    del exception
    return render(
        request,
        'core/404.html',
        {'path': request.path},
        status=HTTPStatus.NOT_FOUND,
    )
