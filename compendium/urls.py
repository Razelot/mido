from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from compendium.models import Demon, Skill
from compendium.api import DemonResource, SkillResource

demon_resource = DemonResource()
skill_resource = SkillResource()

urlpatterns = [
    url(r'^api/', include(demon_resource.urls)),
    url(r'^api/', include(skill_resource.urls)),

    url(r'^demons/$', ListView.as_view(
                    queryset=Demon.objects.all(),
                    template_name="compendium/demons.html")),

    url(r'^skills/$', ListView.as_view(
                    queryset=Skill.objects.all(),
                    template_name="compendium/skills.html")),

    url(r'^demons/(?P<pk>[\w|\W]+)$', DetailView.as_view(
                    model = Demon,
                    template_name="compendium/demon.html")),

    url(r'^skills/(?P<pk>[\w|\W]+)$', DetailView.as_view(
                    model = Skill,
                    template_name="compendium/skill.html")),
]
