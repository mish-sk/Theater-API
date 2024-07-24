from django.contrib import admin
from ticket_service.models import (
    Ticket,
    Reservation,
    Performance
)


admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(Performance)
