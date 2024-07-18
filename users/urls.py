from django.urls import path
from .views import  user_login, user_logout, index, register, edit
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', register, name='register'),
    path('edit', edit, name='edit'),
    ]