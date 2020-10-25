import requests

from django.conf import settings

from project.request_urls import _ADMINISTRATIVE_REGIONS_URL
from project.request_urls import _CITIES_URL
from project.request_urls import _MICRO_REGIONS_URL
from project.request_urls import _REGIONS_URL
from project.request_urls import _RESIDENTIAL_COMPLEXES_URL
from project.request_urls import _STREETS_URL

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def _get_data(
            city='',
            admin_region='',
            region='',
            micro_region='',
            street='',
            res_complex='',
        ) -> dict:
    data = {
        'cities': requests.get(
                f'{settings.BASE_URL}{_CITIES_URL}?search={city}'
            ).json(),
        'admin_regions': requests.get(
                f'{settings.BASE_URL}{_ADMINISTRATIVE_REGIONS_URL}?search={admin_region}'
            ).json(),
        'regions': requests.get(
                f'{settings.BASE_URL}{_REGIONS_URL}?search={region}'
            ).json(),
        'micro_regions': requests.get(
                f'{settings.BASE_URL}{_MICRO_REGIONS_URL}?search={micro_region}'
            ).json(),
        'streets': requests.get(
                f'{settings.BASE_URL}{_STREETS_URL}?search={street}'
            ).json(),
        'res_complexes': requests.get(
                f'{settings.BASE_URL}{_RESIDENTIAL_COMPLEXES_URL}?search={res_complex}'
            ).json(),
    }
    return data




@api_view(['GET'])
def all_locations(request):
    data = _get_data(
        city=request.GET.get('city', ''),
        admin_region=request.GET.get('admin_region', ''),
        region=request.GET.get('region', ''),
        micro_region=request.GET.get('micro_region', ''),
        street=request.GET.get('street', ''),
        res_complex=request.GET.get('res_complex', ''),
    )
    return Response(
        data=data,
        status=status.HTTP_200_OK,
    )




