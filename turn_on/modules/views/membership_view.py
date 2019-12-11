from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View

from accounts.constants import ADMIN
from turn_on.forms import MembershipForm
from turn_on.models import Membership


def correct_user_check(user):
    return user.user_type == ADMIN


class MembershipListView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        memberships = Membership.objects.all()

        context = {
            'page_title': 'Membership List',
            'location': 'membership',
            'memberships': memberships
        }

        return render(request, 'dashboard/membership/list.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class MembershipCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        form = MembershipForm()

        context = {
            'page_title': 'Add Membership',
            'location': 'membership',
            'form': form,
        }

        return render(request, 'dashboard/membership/form.html', context)

    def post(self, request, *args, **kwargs):
        form = MembershipForm(data=request.POST)

        if form.is_valid():
            membership = form.save(commit=False)
            membership.created_by = request.user
            membership.save()

            messages.success(request, 'Membership created!', extra_tags='success')
            return HttpResponseRedirect(reverse('membership_list'))

        else:
            context = {
                'page_title': 'Add Membership',
                'location': 'membership',
                'form': form,
            }

            messages.error(request, form.errors, extra_tags='danger')
            return render(request, 'dashboard/membership/form.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class MembershipUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Membership, pk=kwargs.get('pk', None))
        form = MembershipForm(instance=obj)

        context = {
            'page_title': f'Update {obj}',
            'location': 'membership',
            'form': form,
            'obj': obj
        }

        return render(request, 'dashboard/membership/form.html', context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Membership, pk=kwargs.get('pk', None))
        form = MembershipForm(instance=obj, data=request.POST)

        if form.is_valid():
            membership = form.save(commit=False)
            membership.last_updated_by = request.user
            membership.save()

            messages.success(request, f'{obj} updated!', extra_tags='success')
            return HttpResponseRedirect(reverse('membership_detail', kwargs={'pk': obj.pk}))

        else:
            context = {
                'page_title': f'Update {obj}',
                'location': 'membership',
                'form': form,
                'obj': obj
            }
            messages.error(request, form.errors, extra_tags='danger')
            return render(request, 'dashboard/membership/form.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class MembershipDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Membership, pk=kwargs.get('pk', None))

        context = {
            'page_title': f'Delete {obj}',
            'location': 'membership',
            'obj': obj,
        }

        return render(request, 'dashboard/membership/delete.html', context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Membership, pk=kwargs.get('pk', None))

        obj.delete()
        return HttpResponseRedirect(reverse('membership_list'))

    def test_func(self):
        return correct_user_check(self.request.user)


class MembershipDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Membership, pk=kwargs.get('pk', None))

        context = {
            'page_title': f'Membership Detail: {obj}',
            'location': 'membership',
            'obj': obj
        }

        return render(request, 'dashboard/membership/detail.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)
