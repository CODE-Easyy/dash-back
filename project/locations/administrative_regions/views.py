from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from django.conf import settings 

from .serializers import AdministrativeRegionSerializer

from .models import AdministrativeRegion




class AdminRegionsList(ListAPIView):
    queryset = AdministrativeRegion.objects.all()
    serializer_class = AdministrativeRegionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

                    

class AdminRegionsCreate(CreateAPIView):
    queryset = AdministrativeRegion.objects.all()
    serializer_class = AdministrativeRegionSerializer


class AdminRegionsUpdate(UpdateAPIView):
    queryset = AdministrativeRegion.objects.all()
    serializer_class = AdministrativeRegionSerializer
    lookup_field = 'pk'

class AdminRegionsRemove(DestroyAPIView):
    queryset = AdministrativeRegion.objects.all()
    lookup_field = 'pk'

class AdminRegionsDetail(RetrieveAPIView):
    queryset = AdministrativeRegion.objects.all()
    serializer_class = AdministrativeRegionSerializer
    lookup_field = 'pk'

