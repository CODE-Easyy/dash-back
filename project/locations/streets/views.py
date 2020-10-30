from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


from accounts.permissions import IsAdmin
from accounts.permissions import IsSuperAdmin

from .serializers import StreetSerializer

from .models import Street


class StreetsList(ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]

class StreetCreate(CreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]


class StreetUpdate(UpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]

class StreetRemove(DestroyAPIView):
    queryset = Street.objects.all()
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]

class StreetDetail(RetrieveAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
