from django.urls import path
from .views import get_all, get_by_index

urlpatterns = [
    path('get_all/',get_all),
    path('get_by_index/',get_by_index)
]