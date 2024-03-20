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
from constants import GOOGLE_API_KEY

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

#response = model.generate_content("What is the meaning of life?")
#print(response.text)

app = Flask(__name__)

@app.route("/")
def home_screen():
    return render_template('hp.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/load", methods=['POST'])
def loading_screen():
    user_input = request.form['user_input']
    page = "first"
    description = f"""
    Create a Visual novel choose-your-own-adventure story line with {user_input} as the theme.\
    
    You are a video game script writer. You create the story lines for visual novel games.
    You are being tasked with creating a new script, one based on this theme: {user_input}.
    Create the {page} page of the novel. Do so following these steps:
    1. Deliminate the story text using ---<text>---
    """
    response = model.generate_content(description)
    # Get the response text from the API response
    bot_response = response.text
    session['response'] = response.text
    # Return the response as JSON
    #return jsonify({'bot_response': bot_response})
    return render_template('StartScreen.html')

@app.route('/game/S1')
def game():
    response = session.get('response', 'Default Value')
    return render_template('S1.html', response = response)

if __name__ == '__main__':
    app.run(debug=True)