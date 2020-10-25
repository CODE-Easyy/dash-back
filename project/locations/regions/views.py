from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter

from .serializers import RegionSerializer

from .models import Region


class RegionsList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class RegionCreate(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionUpdate(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'pk'

class RegionRemove(DestroyAPIView):
    queryset = Region.objects.all()
    lookup_field = 'pk'

class RegionDetail(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'pk'