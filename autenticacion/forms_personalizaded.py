
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label=("Dirección de correo"), required=True,
        help_text=("Correo del usuario"))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
