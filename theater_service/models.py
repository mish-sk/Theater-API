from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey("Performance", on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE, related_name="tickets")

    class Meta:
        unique_together = ("row", "seat", "performance",)
        ordering = ["reservation"]

    @staticmethod
    def validate_ticket(row, seat, theater_hall, error_to_raise):
        for ticket_attr_value, ticket_attr_name, theater_hall_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seat_in_the_row"),
        ]:
            count_attrs = getattr(theater_hall, theater_hall_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                        f"number must be in available range: "
                        f"(1, {theater_hall_attr_name}): "
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.performance.theater_hall,
            ValidationError,
        )

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

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

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return self.play.title + " " + str(self.show_time)


class TheaterHall(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.IntegerField()
    seat_in_the_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seat_in_the_row

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField("Genre", blank=True, verbose_name="genres")
    actors = models.ManyToManyField("Actor", blank=True, verbose_name="actors")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
