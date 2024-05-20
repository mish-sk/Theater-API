from django.contrib.auth import get_user_model
from django.db import models


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey("Performance", on_delete=models.CASCADE)
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    def __str__(self):
        return (f"Row: {self.row}, Seat: {self.seat}. "
                f"Performance: {self.performance.play.title}")


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Performance(models.Model):
    play = models.ForeignKey("Play", on_delete=models.CASCADE)
    theater_hall = models.ForeignKey("TheaterHall", on_delete=models.CASCADE)
    show_time = models.DateTimeField()


class TheaterHall(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.IntegerField()
    seat_in_the_row = models.IntegerField()


class Play(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField("Genre", blank=True, verbose_name="plays")
    actors = models.ManyToManyField("Actor", blank=True, verbose_name="plays")


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
