from django.urls import path
from .views import LoginView, SignupView, HomeView, LogoutView

urlpatterns = [
    path('login/', LoginView, name = 'login'),
    path('signup/', SignupView, name = 'signup'),
    path('home/', HomeView, name = 'home'),
    path('logout/', LogoutView, name = 'logout'),
]