from django.urls import path
from . import views as auth

urlpatterns = [
    path('login', auth.AccountLoginView.as_view(), name='account_login_view'),
    path('login/', auth.AccountLoginView.as_view(), name='account_login_view'),
    path('logout', auth.AccountLogoutView.as_view(), name='accounts_logout_view'),
]
