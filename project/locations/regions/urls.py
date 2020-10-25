from django.urls import path

from . import views


urlpatterns = [
    path('list', views.RegionsList.as_view(), name='cities_list'),
    path('detail/<int:pk>', views.RegionDetail.as_view(), name='Region_detail'),
    path('update/<int:pk>', views.RegionUpdate.as_view()),
    path('delete/<int:pk>', views.RegionRemove.as_view()),
    path('create', views.RegionCreate.as_view()),
]
