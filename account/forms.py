from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, University, Major, Consultant, Student


class ConsultantForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=11)
    bachelor_major = forms.ModelMultipleChoiceField(
        queryset=Major.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)
    universities = forms.ModelMultipleChoiceField(
        queryset=University.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)
    identity_code = forms.CharField(required=True, max_length=10)
    master_tendency = forms.CharField(max_length=50, required=False)
    phd_tendency = forms.CharField(max_length=50, required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consultant = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        consultant = Consultant.objects.create(user=user)
        consultant.bachelor_major.add(*self.cleaned_data.get('bachelor_major'))
        consultant.universities.add(*self.cleaned_data.get('universities'))
        consultant.identity_code = self.cleaned_data.get('identity_code')
        consultant.master_tendency = self.cleaned_data.get('master_tendency')
        consultant.phd_tendency = self.cleaned_data.get('phd_tendency')
        consultant.save()
        return user


class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=11)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user

