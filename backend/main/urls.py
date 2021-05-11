from django.urls import path, include

from main import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('consumers/', views.ConsumerList.as_view()),
    path('consumers/<int:pk>/', views.ConsumerDetail.as_view()),
    path('analyzer/<int:pk>/', views.AnalyzerResponse.as_view()),
]

# Página para hacer login
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]