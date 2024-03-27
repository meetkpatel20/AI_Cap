from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template, session
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#from google.colab import userdata
#GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
#GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
from constants import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

format = """The response should be given in the following format:

### Story chapter and title ###
Give the chapter of the story here

### Options ###
1. ** Option 1 title ** Option 1 description (DO NOT LIST A CHAPTER TO GO TO)
2. ** Option 2 title ** Option 2 description (DO NOT LIST A CHAPTER TO GO TO)
...
n. ** Option n title ** Option n description (DO NOT LIST A CHAPTER TO GO TO)"""

breaker = "\n\n############################################\n\n"

# Initial (Chapter 1) prompt -----------------------------------------------------------------------

story_length = ["ten", "six"]

theme = "post-apocalyptic"

person_type = "third"

creature = "an amoeba"

name = "Frank"

# input: story_length, str -> the number of chapters the desired story should eventually reach.
#                             (e.g., "ten" or "six")
#        theme, str        -> the theme of the story (e.g., "post-apocalyptic" or "science fiction")
#        person_type, str  -> the person type the story should be written in (i.e., "first",
#                             "second", or "third")
#        creature, str     -> the creature the protagonist should be (e.g., "human", "rabbit",
#                             "ogre", etc.)
#        name, str         -> the name of the protagonist
# output: p1, str          -> the prompt to send to the model. Includes the intructions for the
#                             model on what to do and the desired format for the model's response
def intro_prompt(story_length, theme, person_type, creature, name):
  instructions = f"""Write the first chapter (out of {story_length} chapters) of a choose-your-own-adventure story
  about {theme}, written in {person_type} person, that ends with a choice for the user to make.
  The choice should have between 2 and 4 options. The protagonist should be {creature} named {name}."""

  p1 = instructions + breaker + format
  return p1

# Chapters 2-n prompt ------------------------------------------------------------------------------

chapter_num = "second"

choice = ""

# input: chapter_num, str -> the number the chapter should be (e.g., "second", "third", etc.)
#        choice, str      -> the choice the user made in the previous chapter, including the title
#                            of the choice, the description, and possibly the number of the choice
#                            (e.g., "1. Do nothing: Decide that it is better to not intervene.")
# output: p2, str         -> the prompt to send to the model. Includes the instructions for the
#                            model on what to do and the format for the model's response
def chapter_prompt(chapter_num, choice, story_length):
  instructions = f"""Write the {chapter_num} chapter (out of {story_length} chapters) of the choose-your-own-adventure story 
  after the user chose to do this action: {choice} 

  Base your response on the previous history.

  The chapter should end in a choice for the user to make. The choice should have 4 options."""

  p2 = instructions + breaker + format
  return p2

# Sentiment Analysis prompt ------------------------------------------------------------------------

sentiment = "safe"

story = '''### Chapter 1: The Mysterious Portal ###

In the lush, emerald depths of a rain-soaked forest, Frogger, a curious frog with a thirst for adventure, hopped along a winding path. As he peered around a bend, a glimmer of light filled his emerald eyes.

Before him lay a shimmering portal, pulsating with an ethereal glow. Intrigued and filled with a pang of trepidation, Frogger approached cautiously. As he drew closer, the portal emitted a faint hum, inviting him inside.

Suddenly, the air around him warped as if reality itself was bending. Frogger felt a surge of adrenaline coursing through his tiny body. He stood at the precipice of a decision that would forever alter his destiny.

### Options ###

1. **Leap Through the Portal:** Step into the shimmering void and discover the mysteries that lie beyond.
2. **Observe from a Distance:** Remain cautious and watch the portal's behavior from afar.
3. **Summon a Friend:** Call upon your fellow amphibians for advice and support.
4. **Turn Back:** Retreat to the safety of the familiar forest, leaving the portal's secrets undisturbed.

### Choice 1 ###
4. **Turn Back:** Retreat to the safety of the familiar forest, leaving the portal's secrets undisturbed.
'''

# input: sentiment, str -> the sentiment the model should use to analyze the user's choices in the
#                          story thus far (e.g., "safe" or "optimistic")
#        story, str     -> entire story thus far, including the chapter titles, bodies, and choices
#                          offered, and the choices made
# output: p3, str       -> the prompt to send to the model. Includes the instructions for the model
#                          on what to do and the format for the model's response
def sentiment(sentiment, story):
  p3 = f"""Generate a sentiment analysis for the choices made in the choose-your-own adventure story below.
  The response should be a single number on a scale from 1-100 based on how {sentiment} the
  choice is, with 100 being the most {sentiment}, and 1 being the least.

  Story:
  {story}"""
  return p3

# Response generation-------------------------------------------------------------------------------

#response = model.generate_content(p1)

#print(response.text)

chat = model.start_chat(history=[])

#response = chat.send_message(intro_prompt(story_length[0], theme, person_type, creature, name))
#print(response.text)
#from pdb import set_trace
#set_trace()
