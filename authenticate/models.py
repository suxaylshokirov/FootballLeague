from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    league_id = models.BigIntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
