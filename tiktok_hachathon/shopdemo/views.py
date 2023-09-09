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

from django.shortcuts import render, redirect
from .forms import VideoForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'videoupload/upload_video.html', {'form': form})


# videoupload/views.py
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})



