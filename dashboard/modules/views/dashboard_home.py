from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views import View

from accounts.constants import ADMIN
from accounts.models import Account


def correct_user_check(user):
    return user.user_type == ADMIN

class DashboardHomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        accounts = Account.objects.all()

        context = {
            'page_title': 'Dashboard Home',
            'location': 'home',
            'accounts': accounts,
        }

        return render(request, 'dashboard/home.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)