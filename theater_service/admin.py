from django.contrib import admin
from theater_service.models import (
    Ticket,
    Reservation,
    Performance,
    TheaterHall,
    Play,
    Actor,
    Genre
)


admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(Performance)
admin.site.register(TheaterHall)
admin.site.register(Play)
admin.site.register(Actor)
admin.site.register(Genre)
