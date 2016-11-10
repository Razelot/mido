from compendium.models import *
import json
import math
import re
import itertools

def map_races():
    json_raw = open("compendium/fixtures/fusion_map.json").read()
    races = json.loads(json_raw)

    for race in races:
        for fusion in races[race]:
            material = re.split(' x ', fusion)
            race_fusion = RaceFusion(
            race_1 = material[0], race_2 = material[1], race = race)
            race_fusion.save()

    json_raw = open("compendium/fixtures/element_map.json").read()
    elements = json.loads(json_raw)

    for element in elements:
        for fusion in elements[element]:
            material = re.split(' x ', fusion)
            race_fusion = RaceFusion(
            race_1 = material[0], race_2 = material[1], race = "Element")
            race_fusion.save()

def fusion_basic():
    demons = Demon.objects.all().exclude(race="Element")
    for demon in demons:
        race_fusions = RaceFusion.objects.all().filter(race=demon.race)
        for race_fusion in race_fusions:
            demons_1 = demons.filter(race=race_fusion.race_1)
            demons_2 = demons.filter(race=race_fusion.race_2)
            for demon_1 in demons_1:
                for demon_2 in demons_2:
                    level_avg = math.ceil(float(demon_1.level + demon_2.level)/2)
                    if level_avg >= demon.level_min and level_avg < demon.level_max:
                        demon_fusion = DemonFusion(
                        demon_1 = demon_1, demon_2 = demon_2, demon = demon)
                        print demon_fusion
                        demon_fusion.save()

def fusion_create_element():
    json_raw = open("compendium/fixtures/element_map.json").read()
    elements = json.loads(json_raw)

    for element in elements:
        demon = Demon.objects.get(name=element)
        for race_fusion in elements[element]:
            material = re.split(' x ', race_fusion)
            materials = Demon.objects.filter(race=material[0])
            pairs = list(itertools.combinations(materials,2))
            for pair in pairs:
                demon_fusion = DemonFusion(
                demon_1 = pair[0], demon_2 = pair[1], demon = demon)
                print(demon_fusion)
                demon_fusion.save()

def fusion_with_element():
    json_raw = open("compendium/fixtures/fusion_element.json").read()
    demons = json.loads(json_raw)

    for demon in demons:
        the_demon = Demon.objects.get(name=demon)
        for fusion in demons[demon]:
            material = re.split(' x ', fusion)
            demon_1 = Demon.objects.get(name=material[0])
            demon_2 = Demon.objects.get(name=material[1])
            demon_fusion = DemonFusion(
            demon_1 = demon_1, demon_2 = demon_2, demon = the_demon)
            print(demon_fusion)
            demon_fusion.save()

def run():
    print("Resetting Database...")
    RaceFusion.objects.all().delete()
    DemonFusion.objects.all().delete()
    print("Mapping Races...")
    map_races()
    print("Basic Fusion...")
    fusion_basic()
    print("Fusing Elements...")
    fusion_create_element()
    print("Elemental Fusion...")
    fusion_with_element()
    print("Complete.")
