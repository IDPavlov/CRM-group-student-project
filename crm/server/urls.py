from django.urls import path
from .views import main_view, registration_view

urlpatterns = [
    path('', main_view, name='manage_main'),
    path('registration/', registration_view)
]