from django.urls import path
from . import views

urlpatterns = [
    path('', views.route_list, name='route_list'),
    path('route/<int:pk>', views.route_detail, name='route_detail'),
]

