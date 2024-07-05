from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
