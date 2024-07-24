import os
import uuid

from django.db import models
from django.utils.text import slugify


class TheaterHall(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.IntegerField()
    seat_in_the_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seat_in_the_row

    def __str__(self):
        return self.name


def play_image_file_path(instance: "Play", filename: str) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/plays/", filename)


class Play(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField("Genre", blank=True, verbose_name="genres")
    actors = models.ManyToManyField("Actor", blank=True, verbose_name="actors")
    image = models.ImageField(null=True, upload_to=play_image_file_path)

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
