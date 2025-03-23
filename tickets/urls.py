from django.urls import path

from tickets.views import TicketListView

app_name = 'tickets'
urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
]
