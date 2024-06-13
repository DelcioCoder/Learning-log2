from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "auth_app"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]