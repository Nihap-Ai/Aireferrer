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



 

image_urls=['../../static/assets/img/temple.jpg','nothing']

R_PROMPT="temple in ruines, forest, stairs, columns, cinematic, detailed, atmospheric, epic, concept art, Matte painting, background, mist, photo-realistic, concept art, volumetric light, cinematic epic + rule of thirds octane render, 8k, corona render, movie concept art, octane render, cinematic, trending on artstation, movie concept art, cinematic composition , ultra-detailed, realistic , hyper-realistic , volumetric lighting, 8k –ar 2:3 –test –uplight"
img_name = R_PROMPT[:12]
def form(request):
    global image_urls,R_PROMPT,img_name

    if request.method == 'POST':
        inp = request.POST.get("inp")
        a_type = request.POST.get("a_type")
        
        print(inp)
        print(a_type)

        type1 = ", cinematic, detailed, atmospheric, epic, concept art, Matte painting, background, mist, photo-realistic, concept art, volumetric light, cinematic epic + rule of thirds octane render, 8k, corona render, movie concept art, octane render, cinematic, trending on artstation, movie concept art, cinematic composition , ultra-detailed, realistic , hyper-realistic , volumetric lighting, 8k –ar 2:3 –test –uplight"
        type2 = ", anthony jones, Loish, painterly style by Gerald parel, craig mullins, marc simonetti, mike mignola, flat colors illustration, bright and colorful, high contrast, Mythology, cinematic, detailed, atmospheric, epic , concept art, Matte painting, Lord of the rings, Game of Thrones, shafts of lighting, mist, , photorealistic, concept art, volumetric light, cinematic epic + rule of thirds | 35mm| octane render, 8k, corona render, movie concept art, octane render, 8k, corona render, cinematic, trending on artstation, movie concept art, cinematic composition , ultra detailed, realistic , hiperealistic , volumetric lighting , 8k –ar 3:1 –test –uplight"
        type3 = ", dreamy ultra wide shot, atmospheric, hyper realistic, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, artstation, rendering by octane, unreal engine –iw 10 –ar 9:16"
        type4 = ", atmospheric, hyper realistic, 8k, epic composition, cinematic, octane render, artstation landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, artstation, rendering by octane, unreal engine —ar 16:9"
        type5 = ", landscape vista photography by Carr Clifton & Galen Rowell, 16K resolution, Landscape veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed landscape painting by Ivan Shishkin, DeviantArt, Flickr, rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, atmospheric, hyper realistic, 8k, epic composition, cinematic, artstation –w 1024 –h 1280"
        type6 = ", volcanic landscape, concept art, octane render, unreal engine 5, trending on artstation, high quality, highly detailed, 8 k hdr, red sea, blue sand, high coherence, path traced, serene landscape, breathtaking landscape, cinematic lighting, hyperrealistic, golden hour"
        type7 = ", cinematic shot, 3d with depth of field, blurred background. female. nautilus. A highly detailed epic cinematic concept art CG render. made in Blender and Photoshop, octane render, excellent composition, cinematic dystopian brutalist atmosphere. dynamic lighting. dramatic lighting. cinematic lighting. aesthetic. stylized. very inspirational. detailed. hq. realistic. warm light. vibrant color scheme. highly detailed. muted colors. Moody. Filmic."
        type8 = "."
        if a_type == "type1":
            art_type = type1;
        elif a_type == "type2":
            art_type = type2;
        elif a_type == "type3":
            art_type = type3;
        elif a_type == "type4":
            art_type = type4;
        elif a_type == "type5":
            art_type = type5;
        elif a_type == "type6":
            art_type = type6;
        elif a_type == "type7":
            art_type = type7;
        elif a_type == "type8":
            art_type = type8;


        else:
            print("Errorrrrrr")
        
      
       
        YOUR_API_TOKEN = "9f720a466712b567cd24f7fe177377f2c961018a"
        PROMPT = inp+art_type
        client = replicate.Client(api_token=YOUR_API_TOKEN)
        model = client.models.get("stability-ai/stable-diffusion")
        image_urls = model.predict(prompt=PROMPT)
        img_name = inp[:12]

        print(PROMPT)
        R_PROMPT = inp
        print(image_urls[0])

    return render(request, "home/Art-Generator.html",{"image_urls": image_urls[0], "PROMPT": R_PROMPT,"img_name": img_name})


 


