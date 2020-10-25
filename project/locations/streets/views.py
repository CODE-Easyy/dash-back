from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter

from .serializers import StreetSerializer

from .models import Street


class StreetsList(ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class StreetCreate(CreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetUpdate(UpdateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    lookup_field = 'pk'

class StreetRemove(DestroyAPIView):
    queryset = Street.objects.all()
    lookup_field = 'pk'

class StreetDetail(RetrieveAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    lookup_field = 'pk'
