from django.shortcuts import render

# Create your views here.
def demon_list(request):
    return render(request, 'compendium/demons.html')
