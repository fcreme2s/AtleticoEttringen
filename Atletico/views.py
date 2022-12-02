from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Route

# Create your views here.

def route_list(request):
    routes = Route.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'atletico/route_list.html', {'routes': routes})


def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'atletico/route_detail.html', {'route': route})