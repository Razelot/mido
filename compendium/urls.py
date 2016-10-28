from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from compendium.models import Demon, Skill
from compendium.api import DemonResource, SkillResource

demon_resource = DemonResource()
skill_resource = SkillResource()

urlpatterns = [
    url(r'^demons/$', ListView.as_view(
                    queryset=Demon.objects.all(),
                    template_name="compendium/demons.html")),

    url(r'^api/', include(demon_resource.urls)),
    url(r'^api/', include(skill_resource.urls)),

    url(r'^demons/(?P<pk>[\w|\W]+)$', DetailView.as_view(
                    model = Demon,
                    template_name="compendium/demon.html")),
]
