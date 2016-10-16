from django.shortcuts import render



from django.views.generic import ListView
from compendium.models import Demon


class DemonView(ListView):
    model = Demon
    template_name = 'demons.html'

    def get_context_data(self, **kwargs):
        ctx = super(DemonView, self).get_context_data(**kwargs)
        ctx['demons'] = Demon.objects.all()
        ctx['races'] = Demon.objects.order_by().values_list('race').distinct()
        return ctx

# Create your views here.
def demon_list(request):
    return render(request, 'compendium/demons.html')
