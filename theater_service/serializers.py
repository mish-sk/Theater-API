from django.core.exceptions import ValidationError
from rest_framework import serializers
from theater_service.models import (
    Ticket,
    Reservation,
    Performance,
    TheaterHall,
    Play,
    Actor,
    Genre,
)


class TicketSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs=attrs)
        Ticket.validate_ticket(
            row=attrs["row"],
            seat=attrs["seat"],
            theater_hall=attrs["performance"].theater_hall,
            error_to_raise=ValidationError,
        )
        return data

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "performance",
            "reservation",
        )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = (
            "id",
            "play",
            "theater_hall",
            "show_time",
        )


class TheaterHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheaterHall
        fields = (
            "id",
            "name",
            "rows",
            "seat_in_the_row",
        )


class PlaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "genres",
            "actors",
        )


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")
