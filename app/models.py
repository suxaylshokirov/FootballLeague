from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, SmallIntegerField, DateTimeField


class League(Model):
    name = CharField(max_length=255)


class Team(Model):
    name = CharField(max_length=255)
    league = ForeignKey('app.League', CASCADE, related_name='teams')
    score = SmallIntegerField(default=0)
    goals = SmallIntegerField(default=0)
    match = SmallIntegerField(default=0)
    win = SmallIntegerField(default=0)
    draw = SmallIntegerField(default=0)
    loss = SmallIntegerField(default=0)
    conceded = SmallIntegerField(default=0)


class Player(Model):
    name = CharField(max_length=255)
    team = ForeignKey('app.Team', CASCADE, related_name='players')


class Match(Model):
    league = ForeignKey('app.League', CASCADE, related_name='matches')
    home_team = ForeignKey('app.Team', CASCADE, related_name='home_matches')
    away_team = ForeignKey('app.Team', CASCADE, related_name='away_matches')
    start_first_time = DateTimeField()
    end_first_time = DateTimeField()
    start_second_time = DateTimeField()
    end_second_time = DateTimeField()
    start_time = DateTimeField()
    home_goal_count = SmallIntegerField()
    away_goal_count = SmallIntegerField()


class Goal(Model):
    player = ForeignKey('app.Player', CASCADE, related_name='goals')
    match_id = ForeignKey('app.Match', CASCADE, 'goals')
    minute = CharField(max_length=10)
