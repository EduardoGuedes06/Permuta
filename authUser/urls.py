from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html '), name="userLogin"),
    path('logout/', auth_views.LogoutView.as_view(), name='userLogout'),
    # path('login/', views.LoginView.as_view(template_name='auth/form.html '), name="userLogin"),
    # path('logout/', views.LogoutView.as_view(), name='userLogout'),
    # path('login/', views.login, name="userLogin"),
    # path('logout/', views.logout, name='userLogout'),
]