from django.urls import path
from . import views

urlpatterns=[
    path('', views.copimage, name = 'copimage'),
    path('views', views.viewImage, name = 'viewImage')
] 