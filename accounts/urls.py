from django.urls import path
from .import views

app_name = 'accounts'

# 회원가입
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
]