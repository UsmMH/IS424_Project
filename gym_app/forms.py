from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import GymClass


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Username',
            'id': 'login-username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Password',
            'id': 'login-password',
        })
    )


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
            'id': 'register-email',
        }),
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name',
            'id': 'register-first-name',
        }),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
            'id': 'register-last-name',
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Choose a username',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }
        ids = {
            'username': 'register-username',
            'password1': 'register-password1',
            'password2': 'register-password2',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            if field_name in ids:
                field.widget.attrs['id'] = ids[field_name]


class GymClassForm(forms.ModelForm):
    class Meta:
        model = GymClass
        fields = [
            'name', 'description', 'instructor', 'category',
            'schedule', 'duration', 'capacity', 'location', 'difficulty',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Morning Power Yoga',
                'id': 'class-name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe what members can expect...',
                'id': 'class-description',
            }),
            'instructor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Instructor full name',
                'id': 'class-instructor',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'id': 'class-category',
            }),
            'schedule': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'id': 'class-schedule',
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minutes',
                'min': 15,
                'id': 'class-duration',
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Max participants',
                'min': 1,
                'id': 'class-capacity',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Studio A, Rooftop Deck',
                'id': 'class-location',
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select',
                'id': 'class-difficulty',
            }),
        }
