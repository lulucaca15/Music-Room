from django.urls import path

from music_controller.api.views import RoomView
from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()),
]