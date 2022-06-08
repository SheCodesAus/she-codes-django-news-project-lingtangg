from django.urls import path, include
from .views import CreateAccountView, profile

app_name = 'users'

urlpatterns = [
  path('create-account/', CreateAccountView.as_view(), name = 'createAccount'),
  path("profile/", profile, name= 'usersProfile'),
]