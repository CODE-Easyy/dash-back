from django.urls import path

from . import views


urlpatterns = [
    path('list', views.CitiesList.as_view(), name='cities_list'),
    path('detail/<int:pk>', views.CityDetail.as_view(), name='city_detail'),
    path('update/<int:pk>', views.CityUpdate.as_view()),
    path('delete/<int:pk>', views.CityRemove.as_view()),
    path('create', views.CityCreate.as_view()),
]
