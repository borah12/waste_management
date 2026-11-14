from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('waste/', views.create_report, name='create_report'),
    path('waste/<int:pk>/', views.report_detail, name='report_detail'),
]