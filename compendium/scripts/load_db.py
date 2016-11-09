import json
import re
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
            strength = demons[demon]['stats']['st'],
            dexterity = demons[demon]['stats']['dx'],
            magic = demons[demon]['stats']['ma'],
            agility = demons[demon]['stats']['ag'],
            luck = demons[demon]['stats']['lu'])
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
            unique_cost=skills[skill]['unique-cost'],
            rank=skills[skill]['rank'])

        # Include description if exists
        if 'description' in skills[skill]:
            new_skill.description = skills[skill]['description']

        new_skill.save()

        # Create demon-skill mapping
        for demon in skills[skill]["demons"]:
            the_demon = Demon.objects.get(name=demon)
            demon_skill = DemonSkill(
                demon = the_demon,
                skill = new_skill,
                level = skills[skill]["demons"][demon])
            demon_skill.save()

def load_fusion():
    json_raw = open("compendium/fixtures/fusion_level.json").read()
    demons = json.loads(json_raw)

    for demon in demons:
        the_demon = Demon.objects.get(name=demon)
        the_demon.level_min = demons[demon]['min_level']
        the_demon.level_max = demons[demon]['max_level']
        the_demon.save()


    json_raw = open("compendium/fixtures/fusion_map.json").read()
    races = json.loads(json_raw)

    for race in races:
        for fusion in races[race]:
            material = re.split(' x ', fusion)
            race_fusion = RaceFusion(
            race_1 = material[0], race_2 = material[1], race = race)
            race_fusion.save()


def run():
    print("Resetting Database...")
    Demon.objects.all().delete()
    Skill.objects.all().delete()
    print("Loading Demons...")
    load_demons()
    print("Loading Fusion...")
    load_fusion()
    print("Loading Skills...")
    load_skills()
    print("Complete.")
