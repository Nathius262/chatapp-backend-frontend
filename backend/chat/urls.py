from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view),
    path('chat/', chat_view, name='chat_view'),
    path('message/', MessageViewSets.as_view()),
    path('friend/', FriendViewSet.as_view())
]
