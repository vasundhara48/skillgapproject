from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze, name='analyze'),
    path('result/<int:pk>/', views.result, name='result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/skills/', views.get_skills_for_role, name='get_skills'),
]
