import json
from compendium.models import *

def load_demons():
    json_raw = open("demons.json").read()

    demons = json.loads(json_raw)

    json_raw = open("compendium/fixtures/demons.json").read()
    demons = json.loads(json_raw)

    for demon in demons:

        # Initialize base demon info
        level = demons[demon]['level']
        race = demons[demon]['race']
        new_demon = Demon(
            name=demon,
            level=level,
            race=race)
        new_demon.save()

        # Set demon resistances
        resistance = Resistance(
            demon = new_demon,
            phys = demons[demon]['resistances']['phys'],
            gun = demons[demon]['resistances']['gun'],
            fire = demons[demon]['resistances']['fire'],
            ice = demons[demon]['resistances']['ice'],
            force = demons[demon]['resistances']['force'],
            elec = demons[demon]['resistances']['elec'],
            light = demons[demon]['resistances']['light'],
            dark = demons[demon]['resistances']['dark']
            )
        resistance.save()

        # Set demon affinities
        phys_afn = demons[demon]['affinities']['phys']
        gun_afn = demons[demon]['affinities']['gun']
        fire_afn = demons[demon]['affinities']['fire']
        ice_afn = demons[demon]['affinities']['ice']
        force_afn = demons[demon]['affinities']['force']
        elec_afn = demons[demon]['affinities']['elec']
        light_afn = demons[demon]['affinities']['light']
        dark_afn = demons[demon]['affinities']['dark']
        almighty_afn = demons[demon]['affinities']['almighty']
        heal_afn = demons[demon]['affinities']['heal']
        ailment_afn = demons[demon]['affinities']['ailment']
        support_afn = demons[demon]['affinities']['support']

        affinity = Affinity(
            demon = new_demon,
            phys = demons[demon]['affinities']['phys'],
            gun = demons[demon]['affinities']['gun'],
            fire = demons[demon]['affinities']['fire'],
            ice = demons[demon]['affinities']['ice'],
            force = demons[demon]['affinities']['force'],
            elec = demons[demon]['affinities']['elec'],
            light = demons[demon]['affinities']['light'],
            dark = demons[demon]['affinities']['dark'],
            almighty = demons[demon]['affinities']['almighty'],
            heal = demons[demon]['affinities']['heal'],
            ailment = demons[demon]['affinities']['ailment'],
            support = demons[demon]['affinities']['support']

            )
        affinity.save()

def run():
    print("hello")
    load_demons()
