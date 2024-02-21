from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),  # Corrected the URL pattern name
    path('about/', views.about, name='about'),
    path('Privacy of policy/', views.about, name='Privacy of policy'),
    path('FAQ/', views.about, name='FAQ'),
    path('Term of use/', views.about, name='Term of use'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
