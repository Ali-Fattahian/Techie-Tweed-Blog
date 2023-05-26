from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name = 'sign-in'),
    path('logout', views.logout_view, name = 'sign-out'),
    path('register', views.SignUpView.as_view(), name = 'sign-up'),
    path('edit-profile/<slug:slug>', views.EditProfileView.as_view(), name = 'edit-profile'),
    path('profiles/<str:username>', views.user_profile, name = 'profile')
]
