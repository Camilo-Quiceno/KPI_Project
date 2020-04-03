"""Users views."""

#Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, DetailView,TemplateView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Profile

#Models
from users.forms import SignupForm
from django.contrib.auth.models import User

class SignupView(FormView):
    """Users sign up view"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin,TemplateView):
    """Profile user view."""

    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

class UptateProfileView(LoginRequiredMixin,UpdateView):
    """Update profile view."""

    template_name = 'users/updateprofile.html'
    model = Profile
    fields = ['picture','trained_in']
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        """Return user`s profile."""
        return self.request.user.profile

class LoginView(auth_views.LoginView):
    """Login view"""

    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'