from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('user', views.user, name='user'),
    path('login', views.login, name='login'),
]
