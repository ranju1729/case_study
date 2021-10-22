from django.urls import path
from .views import get_reddit_titles

urlpatterns = [
    path('fetch_reddit_data/api/v1', get_reddit_titles)
    ]