from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('login/',views.Login_User, name='login'),
    path('login/', auth_views.LoginView.as_view(), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.dashboard, name='dashboard'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name = 'password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset' ),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('register/', views.regester, name= 'register'), 
    path('UserEdit/', views.UserEdit, name= 'UserEdit'), 
    
]