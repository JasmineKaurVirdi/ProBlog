from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('register', views.register_view, name='register'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('login', views.custom_login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('add_post', views.add_post, name="add_post"),
    path('user_posts', views.user_posts, name="user_posts"),
]
