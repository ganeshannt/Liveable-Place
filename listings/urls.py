from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = 'listing_home'),
    path('<int:listing_id>',views.listing, name='listing'),
    path('search',views.search, name = 'search'),
]
