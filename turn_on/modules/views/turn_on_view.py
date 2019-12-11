from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from accounts.constants import ADMIN
from turn_on.forms import TurnOnForm
from turn_on.models import TurnOn


def correct_user_check(user):
    return user.user_type == ADMIN


class TurnOnListView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        turn_on = TurnOn.objects.all()

        context = {
            'page_title': 'Turn On List',
            'location': 'turn_on',
            'turn_on': turn_on,
        }

        return render(request, 'dashboard/turn_on/list.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class TurnOnCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        form = TurnOnForm()

        context = {
            'page_title': 'Add Turn On',
            'location': 'turn_on',
            'form': form,
        }

        return render(request, 'dashboard/turn_on/form.html', context)

    def post(self, request, *args, **kwargs):
        form = TurnOnForm(data=request.POST)

        if form.is_valid():
            turn_on = form.save(commit=False)
            turn_on.created_by = request.user
            turn_on.save()

            messages.success(request, 'Turn on created!', extra_tags='success')
            return HttpResponseRedirect(reverse('turn_on_list'))
        else:
            context = {
                'page_title': 'Add Turn On',
                'location': 'turn_on',
                'form': form,
            }

            messages.error(request, form.errors, extra_tags='danger')
            return render(request, 'dashboard/turn_on/form.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class TurnOnUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(TurnOn, pk=kwargs.get('pk', None))
        form = TurnOnForm(instance=obj)

        context = {
            'page_title': f'Update {obj}',
            'location': 'turn_on',
            'form': form,
            'obj': obj,
        }

        return render(request, 'dashboard/turn_on/form.html', context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(TurnOn, pk=kwargs.get('pk', None))
        form = TurnOnForm(instance=obj, data=request.POST)

        if form.is_valid():
            turn_on = form.save(commit=False)
            turn_on.last_updated_by = request.user
            turn_on.save()

            messages.success(request, f'{obj} updated!', extra_tags='success')
            return HttpResponseRedirect(reverse('turn_on_detail', kwargs={'pk': obj.pk}))

        else:
            context = {
                'page_title': f'Update {obj}',
                'location': 'turn_on',
                'form': form,
                'obj': obj
            }
            messages.error(request, form.errors, extra_tags='danger')
            return render(request, 'dashboard/turn_on/form.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)


class TurnOnDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(TurnOn, pk=kwargs.get('pk', None))

        context = {
            'page_title': f'Delete {obj}',
            'location': 'membership',
            'obj': obj,
        }

        return render(request, 'dashboard/turn_on/delete.html', context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(TurnOn, pk=kwargs.get('pk', None))

        obj.delete()
        return HttpResponseRedirect(reverse('turn_on_list'))

    def test_func(self):
        return correct_user_check(self.request.user)


class TurnOnDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(TurnOn, pk=kwargs.get('pk', None))

        context = {
            'page_title': f'Turn On Detail: {obj}',
            'location': 'membership',
            'obj': obj
        }

        return render(request, 'dashboard/turn_on/detail.html', context)

    def test_func(self):
        return correct_user_check(self.request.user)