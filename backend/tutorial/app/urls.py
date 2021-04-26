from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

# Crea una ruta y registra nuestro viewset.
router = DefaultRouter()
router.register(r'places', views.PlaceViewSet)

# Los API URLs están ahora automáticamente determinados por el router.
urlpatterns = [
    path('demo', views.DemoView.as_view()),
    path('demomatcher', views.DemoMatcher.as_view()),
    path('test', views.TestView.as_view()),
    path('', include(router.urls)),
]