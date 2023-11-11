from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Game(models.Model):
    sequence = models.SmallAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.sequence) + ': ' + self.nome

class Artifact(models.Model):
    sequence = models.SmallAutoField(primary_key=True)
    id = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + ': ' + self.type

class Data(models.Model):
    sequence = models.BigAutoField(primary_key=True)
    id = models.TextField(null=True, blank=True)
    artifact = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    datahora = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return 'Game: ' + str(self.game) + '. ID: ' + str(self.id) + ', Artifact: ' + str(self.artifact) + ', Value: ' + self.value
    