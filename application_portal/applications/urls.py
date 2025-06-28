
from django.urls import path
from  .import views

urlpatterns = [
    path('apply/',views.application_form_view,name ='application_form'),
    path('dashboard/',views.applicant_dashboard,name='applicant_dashboard'),
    path('get-recent-applications/', views.get_recent_applications_json, name='get_recent_applications'),
    path('application-status/',views.application_status_view,name='application_status'),
]
