from tastypie.resources import ModelResource, fields,  ALL, ALL_WITH_RELATIONS
from compendium.models import Demon, Skill, DemonSkill

class DemonResource(ModelResource):
    skills = fields.ToManyField('compendium.api.DemonSkillResource', 'demonskill_set', related_name='demon', full=True, use_in='detail')

    class Meta:
        queryset = Demon.objects.all()
        resource_name = 'demon'
        max_limit = None

class DemonInnerResource(ModelResource):

    class Meta:
        queryset = Demon.objects.all()
        resource_name = 'demon'
        max_limit = None
        excludes = ['race', 'level']

class SkillResource(ModelResource):
    demons = fields.ToManyField('compendium.api.SkillDemonResource', 'demonskill_set', related_name='skill', full=True, use_in='detail')

    class Meta:
        queryset = Skill.objects.all()
        resource_name = 'skill'
        max_limit = None
        excludes = ['demons']

class SkillInnerResource(ModelResource):
    class Meta:
        queryset = Skill.objects.all()
        resource_name = 'skill'
        max_limit = None
        excludes = ['affinity', 'cost', 'rank', 'unique_cost', 'target', 'power', 'hits', 'description']

class DemonSkillResource(ModelResource):
    skill = fields.ToOneField('compendium.api.SkillInnerResource', 'skill', full=True)

    class Meta:
        queryset = DemonSkill.objects.all()
        resource_name = 'demonskill'
        max_limit = None
        excludes = ['id', 'resource_uri']

class SkillDemonResource(ModelResource):
    demon = fields.ToOneField('compendium.api.DemonInnerResource', 'demon', full=True)

    class Meta:
        queryset = DemonSkill.objects.all()
        resource_name = 'demonskill'
        max_limit = None
        excludes = ['id']
