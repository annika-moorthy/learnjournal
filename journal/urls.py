from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resource_generic/', views.ResourceView.as_view(), name='resources'),
    path('resource_create/', views.ResourceCreate.as_view(), name='resource_create'),
    #path(r'resource_update/', views.ResourceUpdate.as_view(), name='resources_update'),
]