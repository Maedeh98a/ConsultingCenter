from django import forms
from django.db import transaction
from django.forms import ModelForm
from account.models import User, University, Major, Consultant, Student


class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        self.fields['username'].help_text = 'نام کاربری شما غیرقابل تغییر است .'
        self.fields['is_consultant'].disabled = True
        self.fields['is_student'].disabled = True

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
            'photo',
            'is_student',
            'is_consultant',
            'show_fullname'
        ]


class EditStudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['description']


class EditConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = [
            'bachelor_major',
            'universities',
            'identity_code',
            'rate_exam',
            'show_rate',
            'interest_major',
            'bachelor_average',
            'master_tendency',
            'phd_tendency',
            'description',
            'consulting_type'
        ]


