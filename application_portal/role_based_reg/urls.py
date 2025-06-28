from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_selection, name='role_selection'),
    path('login-applicant/', views.login_applicant, name='login_applicant'),
    path('login-hr/', views.login_hr, name='login_hr'),
    path('register-applicant/', views.register_applicant, name='register_applicant'),
    path('register-hr/', views.register_hr, name='register_hr'),
]
