# In this file I was trying to get familiar with importing prompt_engineering.py
# and using the variables so that all you would need to clarify are the varibales
# like chapter, name of character, theme, etc., and all the rest of the prompt
# would be pulled from the other file. I also started to work on trying to send
# the model output to history.txt, but that has since been moved to parsing.py

from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template, session
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from prompt_engineering import *
from parsing import parse


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# initializing model
from constants import GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initial (Chapter 1) prompt -----------------------------------------------------------------------

chapter_num = "first"

story_length = ["ten", "six"]

theme = "post-apocalyptic"

person_type = "third"

creature = "an amoeba"

name = "Frank"

# reqs: chapter_num, story_length[], theme, person_type, creature, name
# p1 = prompt + breaker + format

# Chapters 2-n prompt ------------------------------------------------------------------------------

choice = ""

# reqs: chapter_num, story_length[], choice
# p2 = prompt2 + breaker + format

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

# reqs: sentiment, story
# p3 = f"""Generate a sentiment analysis for the choices made in the choose-your-own adventure story below.
# The response should be a single number on a scale from 1-100 based on how {sentiment} the
# choice is, with 100 being the most {sentiment}, and 1 being the least.
# 
# Story:
# {story}"""

# Response generation-------------------------------------------------------------------------------

chat = model.start_chat(history=[])

response = chat.send_message(intro_prompt(story_length[0], theme, person_type, creature))
with open(r"history.txt", "w") as f:
  f.writelines(chat.history) # doesn't work; need to treat it as json
print(response.text)
#from pdb import set_trace
#set_trace()
