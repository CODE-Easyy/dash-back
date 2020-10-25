from django.urls import path

from . import views


urlpatterns = [
    path('list', views.AdminRegionsList.as_view()),
    path('detail/<int:pk>', views.AdminRegionsDetail.as_view()),
    path('update/<int:pk>', views.AdminRegionsUpdate.as_view()),
    path('delete/<int:pk>', views.AdminRegionsRemove.as_view()),
    path('create', views.AdminRegionsCreate.as_view()),
]
