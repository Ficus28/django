from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # <-- Добавили


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls', namespace='pages')), 
    path('accounts/', include('django.contrib.auth.urls')),
]

handler403 = 'blogicum.views.custom_403'
handler404 = 'blogicum.views.custom_404'
handler500 = 'blogicum.views.custom_500'

# Добавляем маршруты для медиафайлов только в режиме отладки (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
