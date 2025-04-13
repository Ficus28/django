from django.urls import path
from .views import AboutPageView, RulesPageView  # Импортируем классы

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # Используем CBV
    path("rules/", RulesPageView.as_view(), name="rules"),
]
