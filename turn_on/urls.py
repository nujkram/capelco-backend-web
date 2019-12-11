from django.urls import path

from turn_on.modules.views import membership_view as membership
from turn_on.modules.views import turn_on_view as turn_on

urlpatterns = [
    # Membership
    path('membership/list', membership.MembershipListView.as_view(), name='membership_list'),
    path('membership/create', membership.MembershipCreateView.as_view(), name='membership_create'),
    path('membership/<pk>/update', membership.MembershipUpdateView.as_view(), name='membership_update'),
    path('membership/<pk>/delete', membership.MembershipDeleteView.as_view(), name='membership_delete'),
    path('membership/<pk>/detail', membership.MembershipDetailView.as_view(), name='membership_detail'),

    # TurnOn
    path('turn-on/list', turn_on.TurnOnListView.as_view(), name='turn_on_list'),
    path('turn-on/create', turn_on.TurnOnCreateView.as_view(), name='turn_on_create'),
    path('turn-on/<pk>/update', turn_on.TurnOnUpdateView.as_view(), name='turn_on_update'),
    path('turn-on/<pk>/delete', turn_on.TurnOnDeleteView.as_view(), name='turn_on_delete'),
    path('turn-on/<pk>/detail', turn_on.TurnOnDetailView.as_view(), name='turn_on_detail'),
]