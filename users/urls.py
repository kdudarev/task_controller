from django.urls import path, include

from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, \
    ShowProfilePageView, EditProfilePageView

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(),
         name='show_profile_page'),
    path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(),
         name='edit_profile_page'),
]