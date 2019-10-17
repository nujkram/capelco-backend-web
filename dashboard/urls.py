from django.urls import path

from dashboard.modules.views import dashboard_home as home_view

urlpatterns = [
    # Dashboard
    path('', home_view.DashboardHomeView.as_view(), name='dashboard_home_view'),
]
