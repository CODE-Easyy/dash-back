from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter

from .serializers import MicroRegionSerializer

from .models import MicroRegion


class MicroRegionsList(ListAPIView):
    queryset = MicroRegion.objects.all()
    serializer_class = MicroRegionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class MicroRegionCreate(CreateAPIView):
    queryset = MicroRegion.objects.all()
    serializer_class = MicroRegionSerializer


class MicroRegionUpdate(UpdateAPIView):
    queryset = MicroRegion.objects.all()
    serializer_class = MicroRegionSerializer
    lookup_field = 'pk'

class MicroRegionRemove(DestroyAPIView):
    queryset = MicroRegion.objects.all()
    lookup_field = 'pk'

class MicroRegionDetail(RetrieveAPIView):
    queryset = MicroRegion.objects.all()
    serializer_class = MicroRegionSerializer
    lookup_field = 'pk'
