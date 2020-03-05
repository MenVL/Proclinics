from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),

    # Редирект и размещение статических файлов
    path('', RedirectView.as_view(url='/catalog/', permanent=True)), ] + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)