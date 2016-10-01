import json

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
        race=race
    )
    new_demon.save()

    # Set demon resistances
    phys_res = demons[demon]['resistances']['phys']
    gun_res = demons[demon]['resistances']['gun']
    fire_res = demons[demon]['resistances']['fire']
    ice_res = demons[demon]['resistances']['ice']
    force_res = demons[demon]['resistances']['force']
    elec_res = demons[demon]['resistances']['elec']
    light_res = demons[demon]['resistances']['light']
    dark_res = demons[demon]['resistances']['dark']


    resistance = Resistance(
        demon = new_demon,
        phys = phys_res,
        fire = fire_res,
        ice = ice_res,
        force = force_res,
        elec = elec_res,
        light = light_res,
        dark = dark_res,
    )
    resistance.save()

    # Set demon affinities

    print(demon)
