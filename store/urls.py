from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('report1', views.report1, name='report1'),
    path('report2', views.report2, name='report2'),
    path('report3', views.report3, name='report3'),
]
