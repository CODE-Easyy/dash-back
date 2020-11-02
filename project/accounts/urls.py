from django.urls import path

from . import views


urlpatterns = [
    path('list', views.ProfilesList.as_view()),
    path('update/<str:code>', views.ProfileUpdate.as_view()),
    path('delete/<str:code>', views.ProfileRemove.as_view()),
    path('detail/<str:code>', views.ProfileDetail.as_view()),
    path('create', views.ProfileCreate.as_view()),
    path('accept', views.accept_new_user),
    path('requests', views.RequestsList.as_view())
]
