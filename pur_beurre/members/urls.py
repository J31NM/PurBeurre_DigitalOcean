from django.urls import path
# from .views import UserRegisterView, UserLoginView
from . import views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('my_account/', views.UserAccountView.as_view(), name='user_account'),
]
