from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


def validate_bracket_size(value):
    if value not in [2, 4, 8, 16, 32, 64, 128, 256]:
        raise ValidationError(
            _(
                "%(value)s is not an acceptable value for bracket size. Acceptable values are 2, 4, 8, 16, 32, 64, 128, 256"
            ),
            params={"value": value},
        )


def validate_players(value):
    bracket_size = value.bracket_size
    next_bracket_size = 2
    while next_bracket_size < bracket_size:
        next_bracket_size *= 2

    if not (value <= bracket_size and value > next_bracket_size):
        raise ValidationError(
            _(
                "The number of players must be less than or equal to the bracket size and greater than the next bracket size down"
            ),
        )


class Tournament(models.Model):
    name = models.CharField("Name", max_length=100)
    bracket_size = models.PositiveSmallIntegerField(validators=[validate_bracket_size])
    players = models.PositiveSmallIntegerField(validators=[validate_players])

    def get_number_of_rounds(self):
        bracket_size = self.bracket_size
        rounds = 0
        while bracket_size > 1:
            bracket_size //= 2
            rounds += 1
        return rounds

    def create_rounds(self):
        number_of_rounds = self.get_number_of_rounds()
        for round_number in range(1, number_of_rounds + 1):
            Round.objects.create(tournament=self, round_number=round_number)

    def __str__(self):
        return self.tournament_name


class Player(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=1)
    name = models.CharField("Name", max_length=100)
    best_song = models.CharField("Best Song", max_length=50)

    def __str__(self):
        return self.name


class Round(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=1)
    round_number = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Round {self.round_number} - {self.tournament}"


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=1)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    player1: models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1")
    player2: models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2")
    winner: models.ForeignKey(Player, on_delete=models.CASCADE, related_name="winner")

    def __str__(self):
        return f"{self.player1} vs {self.player2}"
