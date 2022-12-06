from django.shortcuts import render
from django.views.generic import TemplateView, View
from googletrans import Translator
from apps.processor.forms import ProcessorForm
from django.conf import settings
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import replicate
import time
import mysql.connector


# Create your views here.
class HomeView(TemplateView):
    template_name = "home/index.html"

    
def contact(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        mail = request.POST.get("mail")
        msg = request.POST.get("msg")
        dataBase = mysql.connector.connect(
            host ="containers-us-west-136.railway.app",
            user ="root",
            passwd ="qlK7pZsyw72HKjrvxGU7",
            database ="railway",
            port = "6330"
            )
        cursorObject = dataBase.cursor()
   
        query = "INSERT INTO Contacts (FullName,Mail,Message)\
        VALUES (%s, %s, %s)"
        val = (fname,mail,msg)
             
        cursorObject.execute(query,val)
        dataBase.commit()


        



    return render(request, 'home/page-contact-us.html')

def about(request):
    return render(request, 'home/page-about-us.html')

def donate(request):
        return render(request, 'home/donate.html')
    
def sitemap(request):
        return render(request, 'home/sitemap.html')



 

def form(request):
    if request.method == 'POST':
        inp = request.POST.get("inp")
        
        print(inp)
        
image_urls=['../../static/assets/img/temple.jpg','nothing']
RPROMPT = "nothing"
PROMPT="temple in ruines, forest, stairs, columns, cinematic, detailed, atmospheric, epic, concept art, Matte painting, background, mist, photo-realistic, concept art, volumetric light, cinematic epic + rule of thirds octane render, 8k, corona render, movie concept art, octane render, cinematic, trending on artstation, movie concept art, cinematic composition , ultra-detailed, realistic , hyper-realistic , volumetric lighting, 8k –ar 2:3 –test –uplight"
img_name = PROMPT[:12]
def form(request):
    global image_urls,PROMPT,img_name,RPROMPT

    if request.method == 'POST':
        inp = request.POST.get("inp")
        
        print(inp)
      # DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'railway',
       # 'USER': 'root',
       # 'PASSWORD': 'qlK7pZsyw72HKjrvxGU7',
        #'HOST':'containers-us-west-136.railway.app',
        #'PORT':'6330',
    #}
#}
       
        YOUR_API_TOKEN = "9f720a466712b567cd24f7fe177377f2c961018a"
        PROMPT = inp
        RPROMPT = "mdjrny-v4 style a highly detailed art of "+PROMPT+", 4 k resolution, trending on artstation, masterpiece, smooth, sharp focus,illustration, 8k,Super-Resolution, hyper realistic, super detailed,concept art"
        client = replicate.Client(api_token=YOUR_API_TOKEN)
        model = client.models.get("stability-ai/stable-diffusion")
        image_urls = model.predict(prompt=RPROMPT)
        img_name = PROMPT[:12]

        
        print(image_urls[0])

        dataBase = mysql.connector.connect(
            host ="containers-us-west-136.railway.app",
            user ="root",
            passwd ="qlK7pZsyw72HKjrvxGU7",
            database ="railway",
            port = "6330"
            )
        cursorObject = dataBase.cursor()
   
        query = "INSERT INTO datas (url,prompt)\
        VALUES (%s, %s)"
        val = (image_urls[0],inp)
             
        cursorObject.execute(query,val)
        dataBase.commit()

    return render(request, "home/Art-Generator.html",{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT})

 

def output(request):
    

    return render(request, 'home/Art-generator-output.html',{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT}) 
