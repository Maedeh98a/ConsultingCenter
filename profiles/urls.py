from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    # path('<int:pk>', views.ConsultantProfile.as_view(), name='consultant-profile'),
    # path('', views.Dashboard.as_view(), name='dashboard'),
    path('profile/', views.UserProfile.as_view(), name='user-profile'),
    path('consultant_profile/', views.ConsultantProfile.as_view(), name='consultant-profile'),
    path('student_profile', views.StudentProfile.as_view(), name='student-profile'),
]
