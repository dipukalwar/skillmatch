from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="tracker/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("application/<int:pk>/status/", views.update_status, name="update_status"),
    path("application/<int:pk>/delete/", views.delete_application, name="delete_application"),
    # REST API Endpoint
    path("api/applications/", views.ApplicationListCreateAPI.as_view(), name="api_applications"),
]