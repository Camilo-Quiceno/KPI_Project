"""User forms."""

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form"""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=50 , widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=50 , widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=4, max_length=50)
    last_name = forms.CharField(min_length=4, max_length=50)

    email = forms.CharField(min_length=1, max_length=50,widget=forms.EmailInput())

    def clean_username(self):
        """ Usename must be unique. """
        
        username = self.cleaned_data['username'] #datos que ya limpio python y que los almacena en un dicconario
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
