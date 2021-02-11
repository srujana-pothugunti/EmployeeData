from django.contrib import admin
from django.urls import path
from employeeinfo import views
from employeeinfo import serializers as serializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.Index.as_view(),name='list'),
    path('detail/<pk>',views.Detail.as_view(),name='detail'),
    path('api/users/', serializer.users, name='users'),
]
