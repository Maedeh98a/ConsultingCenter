from django.db import transaction
from django.forms import ModelForm
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UniCommentForm(ModelForm):
    model = UniversityComment
    fields = ['name', 'email', 'body']


class ConsultantCommentForm(ModelForm):
    class Meta:
        model = ConsultantComment
        fields = ['name', 'email', 'body']


class CommentForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AllComment


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=11, required=True)
    subject = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)


