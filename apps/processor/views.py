from django.shortcuts import render
from django.views.generic import TemplateView, View
from googletrans import Translator
from apps.processor.forms import ProcessorForm
from django.conf import settings
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import replicate

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
        
image_urls="nothing"
def form(request):
    global image_urls
    if request.method == 'POST':
        inp = request.POST.get("inp")
        
        print(inp)
       
       
        YOUR_API_TOKEN = "9f720a466712b567cd24f7fe177377f2c961018a"
        PROMPT = inp
        client = replicate.Client(api_token=YOUR_API_TOKEN)
        model = client.models.get("stability-ai/stable-diffusion")
        image_urls = model.predict(prompt=PROMPT)

        

        print(image_urls[0])

    return render(request, "home/form.html",{"image_urls": image_urls[0]})

 

