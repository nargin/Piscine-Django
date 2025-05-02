from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_history_view, name='input_history'),
]