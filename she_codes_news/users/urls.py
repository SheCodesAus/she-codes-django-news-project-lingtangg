from django.urls import path, include
from .views import CreateAccountView, change_password, profile

app_name = 'users'

urlpatterns = [
  path('create-account/', CreateAccountView.as_view(), name = 'createAccount'),
  path("profile/", profile, name= 'usersProfile'),
  path('change-password/', change_password, name='changePassword'),
]