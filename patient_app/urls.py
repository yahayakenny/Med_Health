from django.urls import path
from patient_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('book/', views.book_appointment, name = 'book'),
    path('delete/<int:patient_id>', views.delete, name='patient_delete'),
    path('update/<int:patient_id>', views.update, name='patient_update'),
    path('login/',auth_views.LoginView.as_view(template_name = 'patients/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'patients/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/<int:mypatient_id>', views.patient_detail, name='patient_detail')   
]