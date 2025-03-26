from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from tickets.models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    # template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tickets'
        return context
