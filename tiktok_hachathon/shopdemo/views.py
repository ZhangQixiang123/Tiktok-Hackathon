from typing import Any, Dict
from django.shortcuts import render

# Create your views here.

from .models import Video, Commodity

from django.views import generic

class ShopView(generic.ListView):
    model = Commodity
    template_name = 'shopdemo.html'
    context_object_name = 'commodities'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super(ShopView, self).get_context_data(**kwargs)
    #     # Add additional data to the context dictionary
    #     context['name'] = Commodity.objects.get_queryset
    #     return context

class CommocityDetailView(generic.DetailView):
    model = Commodity
    template_name = 'commodity.html'
    context_object_name = 'commodity'



