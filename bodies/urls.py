from django.urls import path
from . import views

app_name = 'bodies'
urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('success', views.success, name='success'),
    path('services', views.services, name='services'),
    path('about/', views.our_comment, name='about'),
    path('consultant/', views.ConsultantList.as_view(), name='consultant-view'),
    path('<str:slug>', views.consultant_detail, name='consultant-detail'),
    path('university/', views.UniversityList.as_view(), name='university-view'),
    path('<str:slug>/', views.UniversityDetail.as_view(), name='university-detail'),


]