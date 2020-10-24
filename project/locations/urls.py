from django.urls import path, include



urlpatterns = [
    path('locations/', include([ 
        path('cities/', include('locations.cities.urls')),
        path('streets/', include('locations.streets.urls')),
        path('regions/', include('locations.regions.urls')),
        path('micro-regions/', include('locations.micro_regions.urls')),
        path('residential-complexes/', include('locations.residential_complexes.urls')),
        path('administrative-regions/', include('locations.administrative_regions.urls')),

    ]))
]
