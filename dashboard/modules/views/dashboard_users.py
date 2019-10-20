from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.constants import ADMIN
from accounts.models import Account


def correct_user_check(user):
    return user.user_type == ADMIN


class DashboardUserView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()

        context = {
            'page_title': 'Dashboard: Users',
            'location': 'users',
            'accounts': accounts,
        }

        return render(request, 'dashboard/users/home.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)