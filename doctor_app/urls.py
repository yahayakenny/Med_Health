from django.urls import path
from doctor_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
   
    path('<int:doctor_id>', views.doctor_detail, name='doctor_detail'),
    path('map/', views.map, name = 'map' ),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "patients/reset_password.html"), name ='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "patients/password_reset_sent.html"), name ='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "patients/password_reset_form.html"), name ='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "patients/password_reset_done.html"), name ='password_reset_complete'),
    
    path('home/', views.home, name = 'home'),

]