from rest_framework import serializers
from .models import Customer, Tournament, Player, Round, Match


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["pk", "name", "email", "created"]


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["pk", "name", "bracket_size", "players"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["pk", "tournament", "name", "best_song"]


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ["pk", "tournament", "round_number"]


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["pk", "tournament", "round", "player1", "player2", "winner"]
