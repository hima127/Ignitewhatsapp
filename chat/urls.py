from django.urls import path
from chat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carriers/', views.carriers_view, name='carriers'),
    path('careers/<slug:slug>/apply/', views.apply_job, name='apply_job'),   
]
