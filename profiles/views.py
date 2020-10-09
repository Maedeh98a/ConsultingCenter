from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from account.models import *
from .forms import EditStudentForm, EditConsultantForm, EditUserForm


class UserProfile(UpdateView):
    model = User
    template_name = 'profiles/user_profile.html'
    form_class = EditUserForm
    context_object_name = 'user_profile'
    success_url = '/'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class ConsultantProfile(UpdateView):
    model = Consultant
    template_name = 'profiles/consultant_profile.html'
    form_class = EditConsultantForm
    context_object_name = 'consultant_profile'
    # use reverse_lazy
    success_url = '/'

    def get_object(self):
        return Consultant.objects.get(pk=self.request.user.pk)


class StudentProfile(UpdateView):
    model = Student
    form_class = EditStudentForm
    template_name = 'account/edit_profile.html'
    context_object_name = 'student_profile'
    success_url = '/'

    def get_object(self):
        return Student.objects.get(pk=self.request.user.pk)




