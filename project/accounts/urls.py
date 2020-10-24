from django.urls import path

from . import views


urlpatterns = [
    path('list', views.profiles_list),
    path('create', views.create_employee),
    path('update/<str:code>', views.update_employee),
    path('delete/<str:code>', views.remove_employee),
]
