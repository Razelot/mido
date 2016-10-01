from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from compendium.enum import *



class Demon(models.Model):

    name = models.CharField(max_length = 50)
    level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )

    race = models.CharField(
        max_length = 10,
        choices = RACES,
    )

    #flavor_text = models.TextField()

    def __str__(self):
        return self.name

class Resistance(models.Model):

    demon = models.OneToOneField(Demon, default = 0)

    phys = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    gun = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    fire = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    ice = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    force = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    elec = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    light = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    dark = models.CharField(
        max_length = 2,
        choices = RESISTANCES,
        default = NEUTRAL,
    )

    def __str__(self):
        return self.demon.name

class Affinity(models.Model):
    demon = models.OneToOneField(Demon, default = 0)

    phys = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    gun = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    fire = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    ice = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    force = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    elec = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    light = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    dark = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    almighty = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    healing = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    ailment = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )

    support = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)]
    )
