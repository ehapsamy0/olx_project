from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('add_profile/',views.create_profile,name='add_profile'),

    #path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

]