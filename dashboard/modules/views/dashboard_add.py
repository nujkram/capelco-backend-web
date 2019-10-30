from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views import View

from accounts.constants import ADMIN
from accounts.models import Account


def correct_user_check(user):
    return user.user_type == ADMIN

class DashboardAddView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):

        context = {
            'page_title': 'Dashboard Add',
            'location': 'add',
        }

        return render(request, 'dashboard/add.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)