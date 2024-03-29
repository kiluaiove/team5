from django.urls import path
from . import views

app_name = "chart"
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('detail/<str:name>', views.detail, name='detail'),
    path('favors/', views.favors, name='favors'),
    path('guide/', views.guide, name='guide'),
]
