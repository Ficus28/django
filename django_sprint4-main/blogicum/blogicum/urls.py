from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.csrf_failure'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls', namespace='pages')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include([
    path('registration/', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls')), ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'blogicum.views.custom_403'
handler404 = 'blogicum.views.custom_404'
handler500 = 'blogicum.views.custom_500'

