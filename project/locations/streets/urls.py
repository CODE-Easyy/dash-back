from django.urls import path

from . import views


urlpatterns = [
    path('list', views.StreetsList.as_view(), name='cities_list'),
    path('detail/<int:pk>', views.StreetDetail.as_view()),
    path('update/<int:pk>', views.StreetUpdate.as_view()),
    path('delete/<int:pk>', views.StreetRemove.as_view()),
    path('create', views.StreetCreate.as_view()),
]
