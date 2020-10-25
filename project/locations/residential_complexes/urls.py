from django.urls import path

from . import views


urlpatterns = [
    path('list', views.ResidentalComplexesList.as_view(), name='cities_list'),
    path('detail/<int:pk>', views.ResidentalComplexDetail.as_view(), name='ResidentalComplex_detail'),
    path('update/<int:pk>', views.ResidentalComplexUpdate.as_view()),
    path('delete/<int:pk>', views.ResidentalComplexRemove.as_view()),
    path('create', views.ResidentalComplexCreate.as_view()),
]
