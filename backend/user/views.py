from django.shortcuts import render, redirect
from .serializers import CustomGroupSerializers, GroupPaticipantSerializers, ProfileSerializer
from .models import CustomGroup, GroupPaticipant, Profile
from rest_framework.response import Response
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "profile/profile.html")

class ProfileViewSet(generics.ListAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile
    lookup_field = 'id'
    
    def get(self, request, id=None):
        if id == None:
            return redirect('/')
        return self.retrieve(request)
    

class CustomGroupViewSet(generics.ListAPIView):
    serializer_class = CustomGroupSerializers
    queryset = CustomGroup

    def get(self, request):
        return self.list(request)


class GroupPaticipationViewSet(generics.ListAPIView, mixins.RetrieveModelMixin):
    serializer_class = GroupPaticipantSerializers
    queryset = GroupPaticipant
    lookup_field='id'
    permission_classes =[IsAuthenticated]

    def get(self, request, id=None):
        print(request.user)
        return self.retrieve(request)