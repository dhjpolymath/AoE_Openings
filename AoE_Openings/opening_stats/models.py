# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MatchPlayerActions(models.Model):
    match = models.ForeignKey('Matches', on_delete=models.CASCADE)
    player = models.ForeignKey('Players', on_delete=models.CASCADE)
    event_type = models.IntegerField()
    event_id = models.IntegerField()
    time = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = 'match_player_actions'


class Matches(models.Model):
    average_elo = models.IntegerField()
    map_id = models.IntegerField()
    time = models.DateTimeField(blank=True, null=True)
    patch_id = models.FloatField()
    ladder_id = models.IntegerField(blank=True, null=True)
    patch_number = models.IntegerField()
    player1 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name='%(class)s_player1')
    player1_opening_flag0 = models.BooleanField()
    player1_opening_flag1 = models.BooleanField()
    player1_opening_flag2 = models.BooleanField()
    player1_opening_flag3 = models.BooleanField()
    player1_opening_flag4 = models.BooleanField()
    player1_opening_flag5 = models.BooleanField()
    player1_opening_flag6 = models.BooleanField()
    player1_opening_flag7 = models.BooleanField()
    player1_opening_flag8 = models.BooleanField()
    player1_opening_flag9 = models.BooleanField()
    player1_opening_flag10 = models.BooleanField()
    player1_opening_flag11 = models.BooleanField()
    player1_opening_flag12 = models.BooleanField()
    player1_opening_flag13 = models.BooleanField()
    player1_opening_flag14 = models.BooleanField()
    player1_opening_flag15 = models.BooleanField()
    player1_opening_flag16 = models.BooleanField()
    player1_opening_flag17 = models.BooleanField()
    player1_opening_flag18 = models.BooleanField()
    player1_opening_flag19 = models.BooleanField()
    player1_opening_flag20 = models.BooleanField()
    player1_opening_flag21 = models.BooleanField()
    player1_opening_flag22 = models.BooleanField()
    player1_opening_flag23 = models.BooleanField()
    player1_opening_flag24 = models.BooleanField()
    player1_opening_flag25 = models.BooleanField()
    player1_opening_flag26 = models.BooleanField()
    player1_opening_flag27 = models.BooleanField()
    player1_opening_flag28 = models.BooleanField()
    player1_opening_flag29 = models.BooleanField()
    player1_opening_flag30 = models.BooleanField()
    player1_opening_flag31 = models.BooleanField()
    player1_civilization = models.IntegerField()
    player1_victory = models.IntegerField()
    player1_parser_version = models.IntegerField()
    player2 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name='%(class)s_player2')
    player2_opening_flag0 = models.BooleanField()
    player2_opening_flag1 = models.BooleanField()
    player2_opening_flag2 = models.BooleanField()
    player2_opening_flag3 = models.BooleanField()
    player2_opening_flag4 = models.BooleanField()
    player2_opening_flag5 = models.BooleanField()
    player2_opening_flag6 = models.BooleanField()
    player2_opening_flag7 = models.BooleanField()
    player2_opening_flag8 = models.BooleanField()
    player2_opening_flag9 = models.BooleanField()
    player2_opening_flag10 = models.BooleanField()
    player2_opening_flag11 = models.BooleanField()
    player2_opening_flag12 = models.BooleanField()
    player2_opening_flag13 = models.BooleanField()
    player2_opening_flag14 = models.BooleanField()
    player2_opening_flag15 = models.BooleanField()
    player2_opening_flag16 = models.BooleanField()
    player2_opening_flag17 = models.BooleanField()
    player2_opening_flag18 = models.BooleanField()
    player2_opening_flag19 = models.BooleanField()
    player2_opening_flag20 = models.BooleanField()
    player2_opening_flag21 = models.BooleanField()
    player2_opening_flag22 = models.BooleanField()
    player2_opening_flag23 = models.BooleanField()
    player2_opening_flag24 = models.BooleanField()
    player2_opening_flag25 = models.BooleanField()
    player2_opening_flag26 = models.BooleanField()
    player2_opening_flag27 = models.BooleanField()
    player2_opening_flag28 = models.BooleanField()
    player2_opening_flag29 = models.BooleanField()
    player2_opening_flag30 = models.BooleanField()
    player2_opening_flag31 = models.BooleanField()
    player2_civilization = models.IntegerField()
    player2_victory = models.IntegerField()
    player2_parser_version = models.IntegerField()

    class Meta:
        db_table = 'matches'


class Openings(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'openings'


class Players(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'players'
