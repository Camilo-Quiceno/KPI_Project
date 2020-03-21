"""Cases URLS.s"""

#Django
from django.urls import path
from django.views.generic import TemplateView

#views
from cases import views

urlpatterns = [

    # Management
    path(
        route='',
        view=views.CasesFeedView.as_view(),
        name='feed'
    ),
    path(
        route='cases/new/',
        view=views.CasesCreateView.as_view(),
        name='create'
    ),
]