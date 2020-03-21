""" Posts views."""

#Django
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

#Forms
from cases.forms import CaseForm

class CasesFeedView(LoginRequiredMixin,TemplateView):
    template_name = "cases/feed.html"

class CasesCreateView(LoginRequiredMixin, CreateView):
    """Create new post-view"""

    template_name = "cases/new.html"
    form_class = CaseForm
    success_url = reverse_lazy('cases:feed')

    def get_context_data(self,**kwargs):
        """Add user and profile to conext"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


