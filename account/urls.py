from django.urls import path
from account.views import *
from django.contrib.auth import views as auth_views
app_name = 'account'
urlpatterns = [
    path('sign_up', sign_up, name='sign-up'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('reset-password', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('reset-password', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('consultant', SignUpConsultant.as_view(), name='consultant-register'),
    path('student', SignUpStudent.as_view(), name='student-register'),
    # path('<int:pk>/update', EditStudentProfile.as_view(), name='update-student'),

]