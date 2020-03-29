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

    path('cases/updatecase/', views.MyUpdateView,name="updatecase"), 

    path(
        route='cases/listcases/',
        view=views.CasesListView.as_view(),
        name='list'
    ),
]