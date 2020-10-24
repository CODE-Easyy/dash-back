from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProfileListSerializer
from .models import Profile

from project.paginations import TablePagination


@api_view(['GET'])
def profiles_list(request):
    if request.method == 'GET':
        paginator = TablePagination()
        profiles = Profile.objects.all()

        page = paginator.paginate_queryset(profiles, request)
        serializer = ProfileListSerializer(page, many=True)

        return paginator.get_paginated_response(
            serializer.data,
        )

    else:
        return Response(
            {
                'error':  'Only GET responses available!'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


def check_data(data:dict) -> bool:
    _fields = (
        'full_name', 
        'position', 
        'level', 
        'phone', 
        'email',
    )
    for field in _fields:
        if field not in data:
            return False
    return True

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        data = request.data
        if check_data(data):
            if not Profile.check_email(data['email']):
                return Response({
                        'email': 'Profile with such email exists!'
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not Profile.check_phone(data['phone']):
                return Response({
                        'phone': 'Profile with such phone exists!'
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
 
            Profile.create_profile(data=data)
            return Response({
                    'success': 'Employee created successfully!'
                }, 
                status=status.HTTP_200_OK, 
            )
        else:
            return Response({
                    'error': 'Some data didn\'t came!'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response({
                'error':  'Only POST responses available!'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(['PUT'])
def update_employee(request, code=None):
    if request.method == 'PUT':
        profile = Profile.objects.filter(code=code)
        if profile.count() == 0:
            return Response({
                    'error': 'No profile with such code!'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        profile = profile.first()

        data = request.data
        if check_data(data):
            if not profile.email == data['email'].lower():
                if not Profile.check_email(data['email']):
                    return Response({
                            'email': 'Profile with such email exists!'
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            if not profile.phone == data['phone']:
                if not Profile.check_phone(data['phone']):
                    return Response({
                            'phone': 'Profile with such phone exists!'
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            profile.full_name = data['full_name']
            profile.phone = data['phone']
            profile.email = data['email']
            profile.access_level = data['level']
            profile.position = data['position']
            profile.save()
            return Response({
                    'success': 'Employee updated successfully!'
                }, 
                status=status.HTTP_200_OK, 
            )
        else:
            return Response({
                    'error': 'Some data didn\'t came!'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response({
                'error':  'Only PUT responses available!'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(['DELETE'])
def remove_employee(request, code=None):
    if request.method == 'DELETE':
        profile = Profile.objects.filter(code=code)
        if profile.count() == 0:
            return Response({
                    'error': 'No profile with such code!'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile = profile.first()
        profile.delete()
        return Response(
            {
                'success': 'Employee deleted successfully!',
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response({
                'error':  'Only PUT responses available!'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
