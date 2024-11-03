# policies/forms.py
from django import forms
from .models import PolicyHolder,Question
from django import forms
from django.contrib.auth.models import User
from .views import *
class PolicyRequestForm(forms.ModelForm):
    class Meta:
        model = PolicyHolder
        fields = ['user', 'policy']





class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

        return cleaned_data


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ask your question here...'}),
        }
        labels = {
            'question_text': 'Your Question',
        }