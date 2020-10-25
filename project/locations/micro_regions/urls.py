from django.urls import path

from . import views


urlpatterns = [
    path('list', views.MicroRegionsList.as_view(), name='cities_list'),
    path('detail/<int:pk>', views.MicroRegionDetail.as_view(), name='city_detail'),
    path('update/<int:pk>', views.MicroRegionUpdate.as_view()),
    path('delete/<int:pk>', views.MicroRegionRemove.as_view()),
    path('create', views.MicroRegionCreate.as_view()),
]
