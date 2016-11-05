from django.shortcuts import render

from django.core import serializers


from django.views.generic import ListView
from compendium.models import Demon
from django.http import HttpResponse




def demon_json(request):
    object_list = Demon.objects.all() #or any kind of queryset
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')


# class DemonView(ListView):
#     model = Demon
#     template_name = 'demons.html'
#
#     def get_context_data(self, **kwargs):
#         ctx = super(DemonView, self).get_context_data(**kwargs)
#         ctx['demons'] = Demon.objects.all()
#         ctx['races'] = Demon.objects.order_by().values_list('race').distinct()
#         return ctx
#
#         # Create your views here.
#         def demon_list(request):
#             return render(request, 'compendium/demons.html')
