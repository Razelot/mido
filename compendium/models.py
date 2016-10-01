from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from compendium.enum import *



class Demon(models.Model):

    name = models.CharField(max_length = 50)
    level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])

    race = models.CharField(
    max_length = 10,
    choices = RACES)

    #flavor_text = models.TextField()

    def __str__(self):
        return (self.race + ", " + self.name + ", " + str(self.level))

class Stats(models.Model):

    demon = models.OneToOneField(Demon, default = 0)

    hp = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    mp = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    strength = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    dexterity = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    magic = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    agility = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    luck = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )

    def __str__(self):
        return (self.demon.name
        + ": hp:" + str(self.hp)
        + ", mp: " + str(self.mp)
        + ", str: " + str(self.strength)
        + ", dex: " + str(self.dexterity)
        + ", mag: " + str(self.magic)
        + ", agi: " + str(self.agility)
        + ", luk: " + str(self.luck))

class Resistances(models.Model):

    demon = models.OneToOneField(Demon, default = 0)

    phys = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    gun = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    fire = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    ice = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    force = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    elec = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    light = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    dark = models.CharField(
        max_length = 10,
        choices = RESISTANCES,
        default = NEUTRAL
    )

    def __str__(self):
        return (self.demon.name
        + ": phys: " + self.phys
        + ", gun: " + self.gun
        + ", fire: " + self.fire
        + ", ice: " + self.ice
        + ", force: " + self.force
        + ", elec: " + self.elec
        + ", dark: " + self.dark
        + ", light: " + self.light)

class Affinities(models.Model):

    demon = models.OneToOneField(Demon, default = 0)

    phys = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    gun = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    fire = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    ice = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    force = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    elec = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    light = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    dark = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    almighty = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    heal = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    ailment = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    support = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(9), MinValueValidator(-9)])

    def __str__(self):
        return (self.demon.name
        + ": phys: " + str(self.phys)
        + ", gun: " + str(self.gun)
        + ", fire: " + str(self.fire)
        + ", ice: " + str(self.ice)
        + ", force: " + str(self.force)
        + ", elec: " + str(self.elec)
        + ", dark: " + str(self.dark)
        + ", light: " + str(self.light)
        + ", almighty: " + str(self.almighty)
        + ", heal: " + str(self.heal)
        + ", ailment: " + str(self.ailment)
        + ", support: " + str(self.support))

class Skill(models.Model):
    name = models.CharField(max_length = 50)

    affinity = models.CharField(
        max_length = 10,
        choices = AFFINITIES,
        default = 'passsive')

    power = models.CharField(
        max_length = 10,
        choices = POWERS,
        default = '')

    hits = models.CharField(
        max_length = 10,
        default = '')

    target = models.CharField(
        max_length = 10,
        choices = TARGETS,
        default = 'single')

    cost = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)])

    unique_cost = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)])

    rank = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(31), MinValueValidator(1)])

    description = models.TextField()

    def __str__(self):
        return (self.affinity + ", " + self.name)
