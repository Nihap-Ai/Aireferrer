
from django.conf import settings
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

access_token = "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"



def process(inp):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=access_token)
    pipe = pipe.to(device)
    prompt = inp
    with autocast("cuda"):
        image = pipe(prompt, guidance_scale=7.5).images[0]  
    image.save("/outpage/astronaut_rides_horse.png")



