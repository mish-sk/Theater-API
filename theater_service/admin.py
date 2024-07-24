from django.contrib import admin
from theater_service.models import (
    TheaterHall,
    Play,
    Actor,
    Genre
)


admin.site.register(TheaterHall)
admin.site.register(Play)
admin.site.register(Actor)
admin.site.register(Genre)
