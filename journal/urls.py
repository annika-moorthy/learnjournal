from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    #path('resource_generic/', views.ResourceView.as_view(), name='resources'),
    path('resource_create/', views.ResourceCreate.as_view(), name='resource_create'),
    path('search_resources/', views.SearchView.as_view(), name='search'),
    # path('delete_resource/', views.delete_resource, name='delete-id'),
]