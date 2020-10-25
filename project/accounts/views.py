from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView

from rest_framework.response import Response

from .serializers import ProfileListSerializer
from .serializers import ProfileCreateSerializer

from .models import Profile

from project.paginations import TablePagination



class ProfilesList(ListAPIView):
    queryset = Profile.objects.all()
    pagination_class = TablePagination
    serializer_class = ProfileListSerializer

    def get(self, request,*args, **kwargs):
        sort_field = self.request.query_params.get('order', None)
        sign = self.request.query_params.get('sign', None)

        qs = Profile.objects.all()
        paginator = TablePagination()

        if sort_field and sign:
            qs = qs.order_by(sign + sort_field)
        elif sort_field:
            qs = qs.order_by(sort_field)
            
        page = paginator.paginate_queryset(qs, self.request)
        serializer = ProfileListSerializer(
            page, 
            many=True, 
            context={
                'request': request,
            },
        )

        return paginator.get_paginated_response(
            serializer.data,
        )


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

