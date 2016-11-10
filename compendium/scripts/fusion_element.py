from compendium.models import *
import itertools
import json
import re

def element_use():
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

def element_create():
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

def run():
    DemonFusion.objects.all().delete()
    element_create()
    element_use()
