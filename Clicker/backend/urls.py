from django.urls import path
from . import views


boosts = views.BoostViewSet.as_view({ 
    'get': 'list', # Получить список всех бустов 
    'post': 'create', # Создать буст
})

lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update', # редактировать буст
})

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('call_click/', views.call_click),
    path('boosts/', boosts, name='boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('', views.index, name='index'),
]