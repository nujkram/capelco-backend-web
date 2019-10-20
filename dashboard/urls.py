from django.urls import path

from dashboard.modules.views import dashboard_home as home_view
from dashboard.modules.views import dashboard_users as user_view

urlpatterns = [
    # Dashboard
    path('', home_view.DashboardHomeView.as_view(), name='dashboard_home_view'),

    # Users
    path('users/', user_view.DashboardUserView.as_view(), name='dashboard_user_view'),
]
