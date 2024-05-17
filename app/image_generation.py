import json
import requests
from openai import OpenAI

def IMG_Prompt_model(prompt):
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt},
                  {"role": "system",
                      "content": "You are a helpful assistant designed to output JSON."},
                  {"role": "system", "content": """You are a helpful assistant designed to create an image prompt that looks like this: 
                    A realistic painting of a {creature} that is {gender} about {age}. They should have {eye_color} eyes, {hair_color} hair, about {height} tall, and is {emotion}. It should incorporate gradient shading, clean linework, 
                    vibrant palette, and stylized proportions. They should be wearing a {top_color} {top}, {bottom_color} {bottom} that are slightly too big, and {shoes}. The subject of the art should be in this scenario:

                    fill in the spaces between {} with what applies. Base your response on the prompt. The creature can be human, or otherwise stated.
                   """},],
        # {'role': "system", "content": "Here is the history of the chat: " + history}],
    )

    result = stream.model_dump_json()
    data = json.loads(result)
    new_art = {}
    #new_art['chapter'] = data['choices'][0]['message']['content'][0]
    content = data['choices'][0]['message']['content']
    content_data = json.loads(content)
    new_art['gender'] = content_data['gender']
    new_art['age'] = content_data['age']
    new_art['eye_color'] = content_data['eye_color']
    new_art['hair_color'] = content_data['hair_color']
    new_art['height'] = content_data['height']
    new_art['emotion'] = content_data['emotion']
    new_art['top_color'] = content_data['top_color']
    new_art['top'] = content_data['top']
    new_art['bottom_color'] = content_data['bottom_color']
    new_art['bottom'] = content_data['bottom']
    new_art['shoes'] = content_data['shoes']
    new_art['creature'] = content_data['creature']
    return new_art


def img_model(art):
    respo2 = f"""
    Generate an image using this exact template:

    A realistic painting of a {art["gender"]} {art["creature"]} that is {art["age"]}. They should have {art["eye_color"]} eyes, {art["hair_color"]} hair, {art["height"]} size, and is {art["emotion"]}.
    They should be wearing a {art["top_color"]} {art["top"]}, {art["bottom_color"]} {art["bottom"]} that are slightly too big, and {art["shoes"]}. 
    
    The subject of the art should be in this scenario:

    {art["chapter"]}

    Do not add text/words to the image and only make one image.

    """
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=respo2,
        style="vivid",
        size="1024x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    return image_url
