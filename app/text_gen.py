from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
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

def intro_prompt(env):
    theme = env["theme"]
    story_length = env["story_length"]
    person_type = env["person_type"]
    creature = env["creature"]
    name = env["name"]
    chapter_num = env["current_chapter"]
    prompt = f"""
    Write the {chapter_num} chapter (out of {story_length[0]} chapters) of a choose-your-own-adventure story
    about {theme}, written in {person_type} person, that ends with a choice for the user to make.
    The choice should have between 2 and 4 options. The protagonist should be {creature} named {name}.
    """
    return prompt + breaker + format

def mid_prompt(env, choice):
    theme = env["theme"]
    story_length = env["story_length"]
    person_type = env["person_type"]
    creature = env["creature"]
    name = env["name"]
    chapter_num = env["current_chapter"]
    prompt = f"""
    Write the {chapter_num} chapter (out of {story_length[0]} chapters) of the choose-your-own-adventure story 
    after the user chose to do this action: {choice} 
    The chapter should end in a choice for the user to make. The choice should have 4 options."""
    
    return prompt + breaker + format
def model(prompt):
    stream = client.chat.completions.create(
        model="gpt-3.5",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    #return stream
    out = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            out = out + chunk.choices[0].delta.content
    return out
