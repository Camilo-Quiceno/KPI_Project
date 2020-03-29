""" Posts views."""

#Django
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, UpdateView
from django.urls import reverse_lazy, reverse
from django import forms
from django.shortcuts import render
from django.contrib import messages

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

def MyUpdateView(request):
    if request.method == 'POST' and 'update' in request.POST:
        
        case_id = request.POST['case_id']
        
        try:
            case = Case.objects.filter(case_id=case_id).last()
            
            if case:
            
                usercase = case.user
                userrequest = request.user

                if usercase == userrequest:
                    data = request.POST
                    case.step = data['step']
                    case.surgery_type = data['surgery_type']
                    case.is_qc = data['is_qc']
                    case.is_complex = data['is_complex']
                    case.time = data['time']
                    case.is_rejected = data['is_rejected']
                    case.comments = data['comments']
                    case.save()
                    messages.success(request, 'Updated successfully!')  
            else:
                messages.error(request, "Case ID not found, Try again!")

        except:
            messages.error(request, "Case ID not found, Try again!")
            
    elif request.method == 'POST' and 'delete' in request.POST:
        case_id = request.POST['case_id']
        
        try:
            case = Case.objects.filter(case_id=case_id).last()
            
            if case:
            
                usercase = case.user
                userrequest = request.user

                if usercase == userrequest:
                    case.delete()
                    messages.success(request, 'DELETE successfully!')  
            else:
                messages.error(request, "Case ID not found, Try again!")
                
        except:
            messages.error(request, "Case ID not found, Try again!")


    return render(request, 'cases/updatecase.html')

  