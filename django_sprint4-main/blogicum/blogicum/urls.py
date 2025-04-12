from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls', namespace='pages')), 
]

handler403 = 'blogicum.views.custom_403'
handler404 = 'blogicum.views.custom_404'
handler500 = 'blogicum.views.custom_500'
