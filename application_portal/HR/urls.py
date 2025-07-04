from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('get_applications/', views.get_applications, name='get_applications'),
    path('review/', views.review_application, name='review_application'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
