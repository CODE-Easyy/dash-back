from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter

from .serializers import CitySerializer

from .models import City


class CitiesList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class CityCreate(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityUpdate(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'

class CityRemove(DestroyAPIView):
    queryset = City.objects.all()
    lookup_field = 'pk'

class CityDetail(RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'pk'
