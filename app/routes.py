"""
Routes for game engine
"""
import google.generativeai as genai
from openai import OpenAI
from flask import render_template, request, redirect, url_for, session

from app import constants
from app import app
from app.prompt_engineering import chapter_prompt, intro_prompt
from app.parsing import parse

genai.configure(api_key=constants.GOOGLE_API_KEY)
CHAT = genai.GenerativeModel("gemini-pro").start_chat(history=[])

client = OpenAI()
# chat_completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello world"}]
# )

@app.route("/")
@app.route("/start")
def start():
    """
    starting page
    """
    session["current_chapter"] = 0
    session["story_length"] = 1
    session["theme"] = "sci-fi mystery"
    session["person_type"] = "first person"
    session["creature"] = "dragon"
    session["name"] = "Zonpur"

    return render_template("start.html")


@app.route("/begin", methods=["GET"])
def begin():
    """
    first game page
    """
    session["current_chapter"] += 1
    response = CHAT.send_message(
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
    choice4 = parsed_response[2][3]
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
    session["current_chapter"] += 1
    choice_made = request.form["choice-btn"]
    app.logger.info(f"choice_made: {choice_made}")
    response = CHAT.send_message(
        chapter_prompt(
            chapter_num=session["current_chapter"],
            story_length=session["story_length"],
            choice=choice_made,
            random="1",
        )
    )
    parsed_response = parse(response.text)
    title = parsed_response[0]
    body = parsed_response[1]
    choice1 = parsed_response[2][0]
    choice2 = parsed_response[2][1]
    choice3 = parsed_response[2][2]
    choice4 = parsed_response[2][3]
    output = parsed_response[3]
    return render_template(
        "game.html",
        title_head=title[0],
        title_desc=title[1],
        body=body,
        choice1=choice1,
        choice2=choice2,
        choice3=choice3,
        choice4=choice4,
        output=output
    )
