""" Posts views."""

#Django
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, UpdateView
from django.urls import reverse_lazy, reverse
from django import forms

#Models
from cases.models import Case

#Forms
from cases.forms import CaseForm

class CasesFeedView(LoginRequiredMixin,TemplateView):
    template_name = "cases/feed.html"

class CasesListView(LoginRequiredMixin,ListView):
    template_name = "cases/listcases.html"
    model = Case
    ordering = ('created')
    context_object_name = 'cases'

    def get_ordering(self):
        self.order = self.request.GET.get('order', 'asc')
        selected_ordering = self.request.GET.get('ordering', 'created')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self,*args,**kwards):
        context = super(CasesListView,self).get_context_data(*args,**kwards)
        context['current_order'] = self.get_ordering()
        context['order'] = self.order
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

class CaseUpdateView(LoginRequiredMixin,UpdateView):


    template_name = "cases/updatecase.html"
    model = Case
    success_url = "/"
    fields = (
                'step',
                'surgery_type',
                'is_qc',
                'is_complex',
                'is_rejected',
                'time',
                'comments'
        )
    
    
   
    def get_object(self):

        case = self.request.POST.get('case_id')
        if case == None or case =='':
            case_id = self.request.user
        else:
            case_id = Case.objects.filter(case_id=case).exists()
            if case_id:
                case_id = Case.objects.get(case_id=case)
                user = case_id.user.username
                user2=str(self.request.user)
                if user != user2:
                    case_id=self.request.user
            else:
                case_id = self.request.user
        return case_id

  