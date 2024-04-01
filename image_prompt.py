import base64
import os
import requests

engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
#api_key = os.getenv("STABILITY_API_KEY")

#if api_key is None:
#    raise Exception("Missing Stability API key.")

from constants import STABILITY_API_KEY

prompt = """Make an image of the scene described below. Make sure to include all the elements into an image that makes sense:
### Chapter 1: Dragon's Flight ###

The sun peeked over the jagged peaks of the Shadow Mountains, casting an ethereal glow upon the ancient castle perched atop them. I, Johnny, a young drake, stretched my emerald-green wings and basked in the warmth.

A messenger raven arrived, bearing a scroll. It contained word from King Arthur that a great evil threatened the kingdom of Camelot. A sorcerer named Mordred was rallying an army of darkness to overthrow the king.

My heart soared with a mix of excitement and trepidation. I had always dreamed of adventure, and now the time had come."""

prompt2 = """An epic fantasy scene.  A young emerald-green drake with outstretched wings basks in the golden light of sunrise. The drake stands on a weathered stone balcony of an ancient castle perched atop jagged, snow-capped mountains. A black messenger raven with a rolled-up scroll sits on the railing beside the drake."""

prompt3 = """An epic fantasy scene in the style of fantasy art or cinematic. A young emerald-green drake with outstretched wings basks in the golden light of sunrise. The drake stands on a weathered stone balcony of an ancient castle perched atop jagged, snow-capped mountains. A black messenger raven with a rolled-up scroll sits on the railing beside the drake. Below the castle, a vast kingdom stretches out into the distance. The drake has a determined expression on its face."""

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/text-to-image",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {STABILITY_API_KEY}"
    },
    json={
        "text_prompts": [
            {
                "text": prompt2
            }
        ],
        "cfg_scale": 25,
        "height": 768,
        "width": 1344,
        "samples": 1,
        "steps": 30,
        "style_preset": "fantasy-art",
    },
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
