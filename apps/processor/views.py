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
        
        model = replicate.models.get("prompthero/openjourney")
        version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")

# https://replicate.com/prompthero/openjourney/versions/9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb#input
        inputs = {
         'prompt': "mdjrny-v4 style a highly detailed matte painting of a man on a hill watching a rocket launch in the distance by studio ghibli, makoto shinkai, by artgerm, by wlop, by greg rutkowski, volumetric lighting, octane render, 4 k resolution, trending on artstation, masterpiece",

       # Width of output image. Maximum size is 1024x768 or 768x1024 because
       # of memory limits
         'width': 512,

       # Height of output image. Maximum size is 1024x768 or 768x1024 because
       # of memory limits
         'height': 512,

       # Number of images to output
         'num_outputs': 1,
   
       # Number of denoising steps
       # Range: 1 to 500
         'num_inference_steps': 50,

       # Scale for classifier-free guidance
       # Range: 1 to 20
         'guidance_scale': 6,

       # Random seed. Leave blank to randomize the seed
       # 'seed': ...,
       }

     # https://replicate.com/prompthero/openjourney/versions/9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb#output-schema
       output = version.predict(**inputs)
        

        img_name = PROMPT[:12]


        img = image_urls
        img1 = image_urls[0]
        img2 = image_urls[1]
        img3 = image_urls[2]
        img4 = image_urls[3]
        
        print(output)


  


    return render(request, "home/Art-Generator.html",{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT})

 

def output(request):
    

    return render(request, 'home/Art-generator-output.html',{"image_urls": image_urls[0], "PROMPT": PROMPT,"img_name": img_name, "RPROMPT": RPROMPT, "img1": img1, "img2": img2, "img3": img3, "img4": img4, "img": img}) 
