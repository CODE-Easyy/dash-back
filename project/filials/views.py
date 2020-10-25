from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


from .serializers import FilialListSerializer
from .models import Filial

from project.paginations import TablePagination


class FilialListView(ListAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialListSerializer
    pagination_class = TablePagination
    filter_backends = 
