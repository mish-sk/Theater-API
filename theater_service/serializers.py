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


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


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


class PerformanceListSerializer(PerformanceSerializer):
    play_title = serializers.CharField(source="play.title", read_only=True)
    theater_hall_name = serializers.CharField(
        source="theater_hall.name", read_only=True
    )
    theater_hall_capacity = serializers.IntegerField(
        source="theater_hall.capacity", read_only=True
    )
    tickets_available = serializers.IntegerField(read_only=True)

    class Meta:
        model = Performance
        fields = (
            "id",
            "play_title",
            "theater_hall_name",
            "theater_hall_capacity",
            "show_time",
            "tickets_available",
        )


class TheaterHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheaterHall
        fields = (
            "id",
            "name",
            "rows",
            "seat_in_the_row",
            "capacity",
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


class PlayListSerializer(PlaySerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )

    class Meta:
        model = Play
        fields = ("id", "title", "genres", "actors")


class PlayDetailSerializer(PlaySerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "genres",
            "actors",
        )
