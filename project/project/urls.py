from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', include([
        path('accounts/', include('accounts.urls')),
        path('locations/', include('locations.urls')),
        path('filials/', include('filials.urls'))
    ]))
]
