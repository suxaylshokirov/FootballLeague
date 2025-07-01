from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import TextChoices, ForeignKey, CASCADE
from django.db.models.fields import CharField


class User(AbstractUser):
    class RoleType(TextChoices):
        ADMIN = 'admin' , 'Admin'
        REFEREE = 'referee' , 'Referee'
        PLAYER = 'player' , 'Player'

    role = CharField(max_length=255 , choices=RoleType)
    league_id = ForeignKey("app.League" , CASCADE , related_name='users')



