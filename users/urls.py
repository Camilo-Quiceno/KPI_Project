"""Users URLS.s"""

#Django
from django.urls import path
from django.views.generic import TemplateView

#views
from users import views

urlpatterns = [

    # Management
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='profile/',
        view=views.ProfileView.as_view(),
        name='profile'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
]