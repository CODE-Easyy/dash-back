from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.filters import SearchFilter

from .serializers import ResidentalComplexSerializer

from .models import ResidentalComplex


class ResidentalComplexesList(ListAPIView):
    queryset = ResidentalComplex.objects.all()
    serializer_class = ResidentalComplexSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class ResidentalComplexCreate(CreateAPIView):
    queryset = ResidentalComplex.objects.all()
    serializer_class = ResidentalComplexSerializer


class ResidentalComplexUpdate(UpdateAPIView):
    queryset = ResidentalComplex.objects.all()
    serializer_class = ResidentalComplexSerializer
    lookup_field = 'pk'

class ResidentalComplexRemove(DestroyAPIView):
    queryset = ResidentalComplex.objects.all()
    lookup_field = 'pk'

class ResidentalComplexDetail(RetrieveAPIView):
    queryset = ResidentalComplex.objects.all()
    serializer_class = ResidentalComplexSerializer
    lookup_field = 'pk'
