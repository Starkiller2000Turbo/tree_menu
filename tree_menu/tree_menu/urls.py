from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = 'core.views.page_not_found'

urlpatterns = [
    path(
        'menus/',
        include('menus.urls', namespace=apps.get_app_config('menus').name),
    ),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
