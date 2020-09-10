from django.urls import path
from doctor_app import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home', views.home, name = 'home'),
    path('<int:doctor_id>', views.doctor_detail, name='doctor_detail'),
]