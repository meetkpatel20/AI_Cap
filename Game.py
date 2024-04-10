from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template, session
import os

import pathlib
import textwrap

import google.generativeai as genai

#from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown


from openai import OpenAI
from constants import OPENAI_API_KEY
api_key  = os.getenv(OPENAI_API_KEY)
client = OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}
        ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.message["content"]

def gen_img():
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    #return image_url


import os
import requests

def funky():
    payload1 = {
        "animation_prompts": [
        {
            "frame": 0,
            "prompt": "a theropist's face, speaking to wards the camera",
        },
        {
            "frame": 10,
            "prompt": "a theropist's face, speaking to wards the camera",
        },
        {
            "frame": 20,
            "prompt": "a theropist's face, speaking to wards the camera",
        },
        {
            "frame": 30,
            "prompt": "a theropist's face, speaking to wards the camera",
        },
        {
            "frame": 100000000000,
            "prompt": "a theropist's face, speaking to wards the camera",
        },
    ]
    }
    
    payload2 = {
        "input_face": "https://storage.googleapis.com/dara-c1b52.appspot.com/daras_ai/media/f345fcb4-d194-11ee-8804-02420a0001b7/funnymark.jpg",
        "text_prompt": "Vince, I'm hungry can we go eat?",
        #"input_audio": "https://storage.googleapis.com/dara-c1b52.appspot.com/daras_ai/media/8d3f18d4-5f66-11ed-a8a9-02420a0000aa/al-hitchcock-arpa-Merry_Christmas__Jon%203.wav",
    }

    payload3 = {
        "text_prompt": "Innovate a movie poster for a film of a genre of your choosing, such as sci-fi, and give it a title, like ‘Space World’.", 
        "selected_models": ["dream_shaper","protogen_5_3"],
        "dall_e_3_style": "vivid",
        "dall_e_3_quality": "hd",
    }

    response = requests.post(
        "https://api.gooey.ai/v2/art-qr-code/?run_id=4gg2rxtvaa0x&uid=lHPWKyyjdad9MkXueZwWTtCc40r2",
        headers={
            "Authorization": "Bearer sk-F7Bv7NtopXplEjrcFN24SlWYocNaHne3IG953UfdEj6LaZgz" #+ os.environ["GOOEY_API_KEY"],
        },
        json=payload3,
    )
    assert response.ok, response.content

    result = response.json()
    #print(response.status_code, result)
    gemrespo = get_completion("Create a story on pirates")
    print(gemrespo)
    


app = Flask(__name__)

@app.route("/")
def home_screen():
    #funky()
    description = ""
    #get_completion(description)
    gen_img()
    return render_template('hp.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/load", methods=['POST'])
def loading_screen():
    user_input = request.form['user_input']
    page = "first"
    description = f"""
    Create a Visual novel story line with {user_input} as the theme.\
    
    You are a video game script writer. You create the story lines for visual novel games.
    You are being tasked with creating a new script, one based on this theme: {user_input}.
    Create the {page} page of the novel. Do so following these steps:
    1. Deliminate the story text using ---<text>---
    """


    response = get_completion(description)
    # Get the response text from the API response
    bot_response = response
    session['response'] = response
    # Return the response as JSON
    #return jsonify({'bot_response': bot_response})
    return render_template('StartScreen.html')

@app.route('/game/S1')
def game():
    response = session.get('response', 'Default Value')
    return render_template('S1.html', response = response)

if __name__ == '__main__':
    app.run(debug=True)