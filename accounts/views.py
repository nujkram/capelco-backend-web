from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.constants import ADMIN, SUPERADMIN
from accounts.forms import LoginForm
from accounts.models import Account


class AccountLoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm

        context = {
            'page_title': 'Capelco Membership',
            'form': form,
        }

        return render(request, 'account/login.html', context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "User account is not active", extra_tags='danger')
                return HttpResponseRedirect(reverse('account_login_view'))

            login(request, user)
            messages.success(request, "Welcome to Capelco Membership Portal!",
                             extra_tags='success')

            if user.user_type == ADMIN:
                return HttpResponseRedirect(reverse('dashboard_home_view'))
            elif user.user_type == SUPERADMIN:
                return HttpResponseRedirect('/xhDmaaly')
            else:
                return HttpResponseRedirect('account_login_view')
        else:
            messages.error(request, "You have entered an invalid credentials (email and/or password",
                           extra_tags='danger')
            return HttpResponseRedirect(reverse('account_login_view'))


class AccountLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
