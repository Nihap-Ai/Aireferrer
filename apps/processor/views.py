from django.shortcuts import render
from django.views.generic import TemplateView, View
from googletrans import Translator
from apps.processor.forms import ProcessorForm
from django.conf import settings
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/index.html"

    
def contact(request):
    return render(request, 'home/page-contact-us.html')

def about(request):
    return render(request, 'home/page-about-us.html')



def form(request):
    if request.method == 'POST':
        inp = request.POST.get("inp")
        
        print(inp)
        
        access_token = "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"
        
 
        model_id = "CompVis/stable-diffusion-v1-4"
        device = "cuda"
    
        pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=access_token)
        pipe = pipe.to(device)
    
        prompt = inp
        with autocast("cuda"):
            image = pipe(prompt, guidance_scale=7.5).images[0]  
        image.save("/outpage/astronaut_rides_horse.png") 

    return render(request, "home/form.html")

