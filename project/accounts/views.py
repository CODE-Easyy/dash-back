from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

from .serializers import ProfileListSerializer
from .serializers import ProfileCreateSerializer
from .serializers import ProfileDetailSerializer
from .serializers import RequestsSerializer

from .models import Profile

from .permissions import IsAdmin
from .permissions import IsSuperAdmin
from .permissions import SelfOrSuperAdmin

from project.paginations import TablePagination


class RequestsList(ListAPIView):
    queryset = Profile.objects.filter(is_active=False)
    pagination_class = TablePagination
    serializer_class = RequestsSerializer
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]

class ProfilesList(ListAPIView):
    queryset = Profile.objects.all()
    pagination_class = TablePagination
    serializer_class = ProfileListSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def get(self, request,*args, **kwargs):
        print(request.user.full_name)
        print(request.user.is_admin)
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
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]




class ProfileUpdate(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    lookup_field = 'code'
    permission_classes = [
        IsAuthenticated,
        SelfOrSuperAdmin,
    ]

class ProfileRemove(DestroyAPIView):
    queryset = Profile.objects.all()
    lookup_field = 'code'
    permission_classes = [
        IsAuthenticated,
        IsSuperAdmin
    ]

class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'code'
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def accept_new_user(request):
    accept = request.data.get('accept', None)
    code = request.data.get('code', None)

    if (not accept is None) and (not code is None):
        if Profile.objects.filter(code=code).exists():
            p = Profile.objects.get(code=code)  
            if accept:
                p.is_active = True
                p.save()
                return Response({
                    'success': 'Profile accepted successfully'
                })
            else:
                p.delete()
                return Response({
                    'success': 'Profile deleted successfully.'
                })
        else:
            return Response({
                'error': 'Profile with such code doesn\'t exist'
            })
    else:
        return Response({
            'error': 'Acceptance or code of profile did\'n came'
        })