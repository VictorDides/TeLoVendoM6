from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='pagina_bienvenida'),
    path('tweet/', views.createTweet, name='tweet'),
]