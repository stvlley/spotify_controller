from django.urls import path

from .models import Room
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
  
]
