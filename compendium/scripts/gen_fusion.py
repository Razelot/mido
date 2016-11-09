from compendium.models import *
import math

def run():
    DemonFusion.objects.all().delete()

    demons = Demon.objects.all()

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
