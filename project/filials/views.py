from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import FilialListSerializer
from .models import Filial

from project.paginations import TablePagination

from accounts.permissions import IsAdmin
from accounts.permissions import IsSuperAdmin

class FilialListView(ListAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialListSerializer
    pagination_class = TablePagination
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def get(self, request, *args, **kwargs):
        name = self.request.query_params.get('name', '')
        city = self.request.query_params.get('city', '')
        address = self.request.query_params.get('address', '')
        search = self.request.query_params.get('search', None)
        qs = Filial.objects.all()
        

        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(city__name__icontains=search) |
                Q(actual_address__icontains=search)            
            ) 
        else :
            qs = qs.filter(
                name__icontains=name,
                city__name__icontains=city,
                actual_address__icontains=address,
            )

        paginator = TablePagination()
        page = paginator.paginate_queryset(qs, self.request)


        serializer = FilialListSerializer(
            page, 
            many=True, 
            context={
                'request': request,
            },
        )
        return paginator.get_paginated_response(
            serializer.data,
        )