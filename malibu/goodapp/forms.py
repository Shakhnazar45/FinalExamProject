from django import forms
from .models import Market
from django.contrib.auth.forms import AuthenticationForm,UsernameField


class ProductForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = '__all__'

class LoginForm(AuthenticationForm):
        def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)

        username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),label='')
        password = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), label='')