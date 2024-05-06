from openai import OpenAI
import requests
import json
client = OpenAI()
breaker = "\n\n############################################\n\n"
format = """The response should be given in the following format:

### Story chapter and title ###
Give the chapter of the story here

### Options ###
1. ** Option 1 title ** Option 1 description (DO NOT LIST A CHAPTER TO GO TO)
2. ** Option 2 title ** Option 2 description (DO NOT LIST A CHAPTER TO GO TO)
...
n. ** Option n title ** Option n description (DO NOT LIST A CHAPTER TO GO TO)"""

image = """Based on the chapter's details, create a description in great detail about an image that would represent the current chapter

### Description ###
Put the description here
"""

def intro_prompt(env):
    theme = env["theme"]
    story_length = env["story_length"]
    person_type = env["person_type"]
    creature = env["creature"]
    name = env["name"]
    chapter_num = env["current_chapter"]
    prompt = f"""
    Write the {chapter_num} chapter (out of {story_length} chapters) of a choose-your-own-adventure story
    about {theme}, written in {person_type} person, that ends with a choice for the user to make.
    The choice should have between 2 and 4 options. The protagonist should be {creature} named {name}.
    """
    return prompt + breaker + format + image

def mid_prompt(env, choice):
    story_length = env["story_length"]
    chapter_num = env["current_chapter"]
    prompt = f"""
    Write the {chapter_num} chapter (out of {story_length[0]} chapters) of the choose-your-own-adventure story 
    after the user chose to do this action: {choice} 
    The chapter should end in a choice for the user to make. The choice should have 4 options."""
    
    return prompt + breaker + format + image
def IMG_Prompt_model(prompt):
    #print(prompt)
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                  {"role": "system", "content": """You are a helpful assistant designed to create an image prompt that looks like this: 
                    A realistic painting of a {creature} that is {gender} about {age}. They should have {eye_color} eyes, {hair_color} hair, about {height} tall, and is {emotion}. It should incorporate gradient shading, clean linework, 
                    vibrant palette, and stylized proportions. They should be wearing a {top_color} {top}, {bottom_color} {bottom} that are slightly too big, and {shoes}. The subject of the art should be in this scenario:

                    fill in the spaces between {} with what applies. Base your response on the prompt. The creature can be human, or otherwise stated.
                   """},],
                  #{'role': "system", "content": "Here is the history of the chat: " + history}],
    )
    

    print(stream)
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
    return(new_art)
    #return result.choices[0].message.content
    #return result['choices'][0]['message'].strip()

def IMG_Prompt_gen(prompt):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                  {"role": "system", "content": "Based on the prompt provided, write one sentence describing the scenario."},],
                  #{'role': "system", "content": "Here is the history of the chat: " + history}],
    )
    

    print(stream.choices[0].message.content)
    return stream.choices[0].message.content
def img_model(art):
    respo2 = f"""
    Generate an image using this exact template:

    A realistic painting of a {art["gender"]} {art["creature"]} that is {art["age"]}. They should have {art["eye_color"]} eyes, {art["hair_color"]} hair, {art["height"]} size, and is {art["emotion"]}.
    They should be wearing a {art["top_color"]} {art["top"]}, {art["bottom_color"]} {art["bottom"]} that are slightly too big, and {art["shoes"]}. 
    
    The subject of the art should be in this scenario:

    {art["chapter"]}

    Do not add text to the painting and only make one image.

    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=respo2,
        style='vivid',
        size="1024x1024",
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url
    response = requests.get(image_url)
    print(response)
    print (image_url)
    return image_url

