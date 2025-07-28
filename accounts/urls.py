from django.urls import path, re_path, include
from .views import login_view, register_view, logout_view, CustomPasswordResetView, CustomPasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include('django.contrib.auth.urls')),
]