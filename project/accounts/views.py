from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView

from .serializers import ProfileListSerializer
from .serializers import ProfileCreateSerializer

from .models import Profile

from project.paginations import TablePagination



class ProfilesList(ListAPIView):
    queryset = Profile.objects.all()
    pagination_class = TablePagination
    serializer_class = ProfileListSerializer

class ProfileCreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer


class ProfileUpdate(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    lookup_field = 'code'

class ProfileRemove(DestroyAPIView):
    queryset = Profile.objects.all()
    lookup_field = 'code'

class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    lookup_field = 'code'

