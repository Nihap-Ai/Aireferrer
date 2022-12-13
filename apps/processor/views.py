from django.shortcuts import render
from django.views.generic import TemplateView, View
from googletrans import Translator
from apps.processor.forms import ProcessorForm
from django.conf import settings
import replicate
import time
import mysql.connector
from django.core.files.storage import FileSystemStorage

 


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

def test(request):
    return render(request, 'home/test.php')

def donate(request):
        return render(request, 'home/donate.html')
def sitemap(request):
        return render(request, 'home/urllist.txt')



 

def form(request):
    if request.method == 'POST':
        inp = request.POST.get("inp")
        
        print(inp)

image_urls = ['../../static/assets/img/temple.jpg','https://replicate.delivery/pbxt/60HaZWg8c852FlStYs8D51ypzmRAp0Xg4gcZfSZk6T1AuoEIA/out-1.png','https://replicate.delivery/pbxt/tM1Z4CjNUfT8M6VqMmHC77pK6PUof3LtqwLv33Aa9y8BcRJQA/out-2.png','https://replicate.delivery/pbxt/W5gJjwPxu14dE5AuMEBNSswIfvdIbVt9IVMjXN3tPnMBuoEIA/out-3.png']
img = image_urls
img1 = image_urls[0]
img2 = image_urls[1]
img3 = image_urls[2]
img4 = image_urls[3]
RPROMPT = "nothing"
PROMPT="temple in ruines, forest, stairs, columns, cinematic, detailed, atmospheric, epic, concept art, Matte painting, background, mist, photo-realistic, concept art, volumetric light, cinematic epic + rule of thirds octane render, 8k, corona render, movie concept art, octane render, cinematic, trending on artstation, movie concept art, cinematic composition , ultra-detailed, realistic , hyper-realistic , volumetric lighting, 8k –ar 2:3 –test –uplight"
img_name = PROMPT[:12]
def form(request):
    global image_urls,PROMPT,img_name,RPROMPT,img1,img2,img3,img4,img

    if request.method == 'POST':
        inp = request.POST.get("inp")
        file = request.FILES.get("init")

       #
        
        print(file)
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
        model = client.models.get("prompthero/openjourney")
        version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")
        image_urls = model.predict(prompt=RPROMPT,num_outputs=4)
        

        img_name = PROMPT[:12]


        img = image_urls
        img1 = image_urls[0]
        img2 = image_urls[1]
        img3 = image_urls[2]
        img4 = image_urls[3]
        
        print(img)


  

        #dataBase = mysql.connector.connect(
       #     host ="containers-us-west-136.railway.app",
        #    user ="root",
       #     passwd ="qlK7pZsyw72HKjrvxGU7",
        #    database ="railway",
         #   port = "6330"
         #   )
       # cursorObject = dataBase.cursor()   
   
       # query = "INSERT INTO datas (url,prompt)\
       # VALUES (%s, %s)"
       # val = (image_urls[0],inp)
             
        #cursorObject.execute(query,val)
        #dataBase.commit()

    return render(request, "home/Art-Generator.html",{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT})

 

def output(request):
    

    return render(request, 'home/Art-generator-output.html',{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT, "img1": img1, "img2": img2, "img3": img3, "img4": img4, "img": img}) 
