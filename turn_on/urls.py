from django.urls import path

from turn_on.modules.views import membership_view as membership

urlpatterns = [
    # Membership
    path('membership/list', membership.MembershipListView.as_view(), name='membership_list'),
    path('membership/create', membership.MembershipCreateView.as_view(), name='membership_create'),
    path('membership/<pk>/update', membership.MembershipUpdateView.as_view(), name='membership_update'),
    path('membership/<pk>/delete', membership.MembershipDeleteView.as_view(), name='membership_delete'),
    path('membership/<pk>/detail', membership.MembershipDetailView.as_view(), name='membership_detail'),
]