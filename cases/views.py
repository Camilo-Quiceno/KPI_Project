""" Posts views."""

#Django
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy

#Models
from cases.models import Case

#Forms
from cases.forms import CaseForm

class CasesFeedView(LoginRequiredMixin,TemplateView):
    template_name = "cases/feed.html"

class CasesListView(LoginRequiredMixin,ListView):
    template_name = "cases/listcases.html"
    model = Case
    ordering = ('-created')
    context_object_name = 'cases'

    def get_ordering(self):
        return self.request.GET.get('ordering','-created')

    def get_context_data(self,*args,**kwards):
        context = super(CasesListView,self).get_context_data(*args,**kwards)
        context['current_order'] = self.get_ordering()
        return context

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


