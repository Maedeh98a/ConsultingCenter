from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .decorators import student_required, consultant_required
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from .forms import ConsultantForm, StudentForm
from .models import User, Student, Consultant


def home(request):
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'account/sign_up.html')

# class SignUpConsultant(CreateView):
#     model = User
#     form_class = ConsultantForm
#     template_name = 'account/consultant_register.html'
#     second_form_class = UserCreationForm
#
#     def get_context_data(self, **kwargs):
#         context = super(SignUpConsultant, self).get_context_data(**kwargs)
#         context['user_form'] = self.second_form_class
#         return context
#
#     def form_valid(self, form):
#         user_form = UserCreationForm(self.request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             consultant = form.save(commit=False)
#             consultant.user_id = user.id
#             consultant.save()
#         return HttpResponseRedirect(self.get_success_url())


class SignUpConsultant(CreateView):
    model = User
    form_class = ConsultantForm
    template_name = 'account/consultant_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_types'] = 'consultant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class SignUpStudent(CreateView):
    model = User
    form_class = StudentForm
    template_name = 'account/student_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_types'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('account:login')


