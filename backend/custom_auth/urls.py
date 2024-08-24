from django.urls import path
from .views import RegisterView, LoginView, GetUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-users/', GetUserView.as_view(), name='get-users')
]