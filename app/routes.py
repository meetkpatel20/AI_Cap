"""
Routes for game engine
"""
import google.generativeai as genai
from flask import render_template, request, redirect, url_for, session

from app import constants
from app import app
from app.prompt_engineering import chapter_prompt, intro_prompt
from app.parsing import parse
from app import text_gen

genai.configure(api_key=constants.GOOGLE_API_KEY)
CHAT = genai.GenerativeModel("gemini-pro").start_chat(history=[])


@app.route('/')
@app.route('/start')
def start():
    """
    starting page
    """
    session["current_chapter"] = 0
    session["story_length"] = 1
    session["theme"] = "school"
    session["person_type"] = "student"
    session["creature"] = "human"
    session["name"] = "Jake"
    return render_template("start.html")


@app.route("/begin", methods=["GET"])
def begin():
    """
    first game page
    """
    session["current_chapter"] += 1
    prompt = text_gen.intro_prompt(session)
    text_gen.model(prompt)

    """response = CHAT.send_message(
        intro_prompt(
            session["story_length"],
            session["theme"],
            session["person_type"],
            session["creature"],
            session["name"]
        )
    )
    parsed_response = parse(response.text)
    title = parsed_response[0]
    body = parsed_response[1]
    choice1 = parsed_response[2][0]
    choice2 = parsed_response[2][1]
    choice3 = parsed_response[2][2]
    choice4 = parsed_response[2][3]"""
    # title = (100, "TESTING")
    # body = "Lorem ipsum dolor sit amet, consectetur et est culpa et culpa duis."
    # choice1 = "test"
    # choice2 = "test test"
    # choice3 = "test test test"
    # choice4 = "test test test test"

    return render_template(
        "begin.html",
        title_head=session["current_chapter"],
        title_desc=title[1],
        body=body,
        choice1=choice1,
        choice2=choice2,
        choice3=choice3,
        choice4=choice4,
    )


@app.route("/game", methods=["POST"])
def game():
    """
    Game page
    """
    if request.method == 'GET':
        # response = call_gemini.generate_content()
        response = "TEST TEXT"
        return render_template('game.html', response=response)
    if request.method == 'POST':
        # response = call_gemini.generate_content()
        response = "TEST TEXT"
        return render_template('game.html', response=response)
    return None


@app.route('/refresh', methods=['POST'])
def refresh():
    """"""
    return redirect(url_for('game'))
