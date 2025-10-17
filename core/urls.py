# urls.py
from django.urls import path
from .views import NthNodeAPIView, LongestNodeAPIView, ShortestNodeBetweenAPIView

urlpatterns = [
    path('nth-node/', NthNodeAPIView.as_view()),
    path('longest-node/', LongestNodeAPIView.as_view()),
    path('shortest-between/', ShortestNodeBetweenAPIView.as_view()),
]