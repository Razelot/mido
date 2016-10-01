import json
from compendium.models import *

def load_demons():
    json_raw = open("compendium/fixtures/demons.json").read()
    demons = json.loads(json_raw)

    for demon in demons:
        # Initialize base demon info
        new_demon = Demon(
            name=demon,
            level=demons[demon]['level'],
            race=demons[demon]['race'])
        new_demon.save()

        # Set demon stats
        stats = Stats(
            demon = new_demon,
            hp = demons[demon]['stats']['hp'],
            mp = demons[demon]['stats']['mp'],
            strength = demons[demon]['stats']['strength'],
            dexterity = demons[demon]['stats']['dexterity'],
            magic = demons[demon]['stats']['magic'],
            agility = demons[demon]['stats']['agility'],
            luck = demons[demon]['stats']['luck'])
        stats.save()

        # Set demon resistances
        resistances = Resistances(
            demon = new_demon,
            phys = demons[demon]['resistances']['phys'],
            gun = demons[demon]['resistances']['gun'],
            fire = demons[demon]['resistances']['fire'],
            ice = demons[demon]['resistances']['ice'],
            force = demons[demon]['resistances']['force'],
            elec = demons[demon]['resistances']['elec'],
            light = demons[demon]['resistances']['light'],
            dark = demons[demon]['resistances']['dark'])
        resistances.save()

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

        affinities = Affinities(
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
            support = demons[demon]['affinities']['support'])
        affinities.save()

def load_skills():
    json_raw = open("compendium/fixtures/skills.json").read()
    skills = json.loads(json_raw)

    for skill in skills:
        # Initialize skill info
        new_skill = Skill(
            name=skill,
            affinity=skills[skill]['affinity'],
            power=skills[skill]['power'],
            hits=skills[skill]['hits'],
            target=skills[skill]['target'],
            cost=skills[skill]['cost'],
            unique_cost=skills[skill]['unique_cost'],
            rank=skills[skill]['rank'])

        if 'description' in skills[skill]:
            new_skill.description = skills[skill]['description']

        new_skill.save()

        # Create demon-skill mapping
        for demon in skill[skills][demon]:
            #TODO

def run():
    print("hello")
    #load_demons()
    load_skills()
