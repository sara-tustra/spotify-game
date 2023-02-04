from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField("Name", max_length=50)
    bracket_size = models.IntegerField(default=32)
    players = models.IntegerField()


class Round(models.Model):
    match_id = models.IntegerField()
    round = models.IntegerField()


class Player(models.Model):
    name = models.CharField("Name", max_length=50)
    best_song = models.CharField("Best Song", max_length=50)


class Game(models.Model):
    round_id = models.IntegerField()
    players = models.ForeignKey(Player, on_delete=models.CASCADE)
