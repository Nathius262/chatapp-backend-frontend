
from django.urls import path
from .views import GroupPaticipationViewSet, ProfileViewSet, profile_view

app_name = "user"

urlpatterns = [
    path('group/<int:id>/', GroupPaticipationViewSet.as_view(), name="group_paticipant"),
    path('profile/', profile_view, name='user_profile'),
    path('profile/<int:id>/', ProfileViewSet.as_view(), name="profile"),
]