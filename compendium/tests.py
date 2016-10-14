from django.test import TestCase
from compendium.models import Demon
import json

class CompendiumTest(TestCase):
    def load_demons(self):
        json_raw = open("compendium/fixtures/demons.json").read()
        demons = json.loads(json_raw)

        for demon in demons:
            level = demons[demon]['level']
            race = demons[demon]['race']
            new_demon = Demon(
            name=demon,
            level=level,
            race=race)

    print("Demons loaded sucessfuly!")
