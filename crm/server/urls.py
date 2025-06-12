from django.urls import path
from views import main

urlpatterns = [
    path('manage/main/', main, name='manage_main')
]