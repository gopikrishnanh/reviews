from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('Movie/<int:Movie_id>',views.details,name='dt'),
    path('search',views.search,name='search')
]