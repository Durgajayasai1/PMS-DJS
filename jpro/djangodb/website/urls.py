from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signup1',views.signup1,name="signup"),
    path('login',views.login,name="login"),
    path('login1',views.login1,name="login"),
    path('project',views.project,name="project"),
    path('todo', views.todo,name="todo"),
    path('sidebar',views.sidebar,name="sidebar"),
    path('inhome', views.inhome, name="inhome"),
    path('contactus', views.contactus, name="contactus"),
    path('profile', views.profile, name="profile")
]
