from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('resource_create/', views.ResourceCreate.as_view(), name='resource_create'),
    path('search_resources/', views.SearchView.as_view(), name='search'),
    path('updateresource/<int:pk>', views.ResourceUpdateView.as_view(), name='Resource_update_form'),
]
