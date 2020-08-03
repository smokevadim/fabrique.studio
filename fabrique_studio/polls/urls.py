from django.urls import path
from .views import *

app_name = "polls"

urlpatterns = [
    path('polls/', PollView.as_view()),
    path('polls/<int:pk>', SinglePollView.as_view()),
    path('my_polls', MyPollView.as_view()),
]