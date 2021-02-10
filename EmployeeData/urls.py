from django.contrib import admin
from django.urls import path
from employeeinfo import views
from employeeinfo import serializers as serializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.index,name='list'),
    path('api/users/', serializer.users, name='users'),
]
