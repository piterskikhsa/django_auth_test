from django.urls import path
from django.contrib.auth import views as auth_views

from simpleapp import views

app_name = 'simple_app'
urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.index, name='index'),
]
