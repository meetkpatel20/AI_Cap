from openai import OpenAI

client = OpenAI()

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
    return prompt
def model(prompt):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
