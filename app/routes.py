"""
Routes for game engine
"""
from os import walk
import google.generativeai as genai
from flask import render_template, request, redirect, url_for, session

from app import constants
from app import app
from app.prompt_engineering import chapter_prompt, intro_prompt
from app.parsing import parser

genai.configure(api_key=constants.GOOGLE_API_KEY)
CHAT = genai.GenerativeModel("gemini-pro").start_chat(history=[])


@app.route("/")
@app.route("/start")
def start():
    """
    starting page
    """
    session["story_length"] = 1
    session["theme"] = "school"
    session["person_type"] = "student"
    session["creature"] = "human"
    session["name"] = "Jake"

    return render_template("start.html")


@app.route("/game", methods=["GET", "POST"])
def game():
    """
    Game page
    """
    if request.method == "GET":
        response = CHAT.send_message(
            intro_prompt(
                session["story_length"],
                session["theme"],
                session["person_type"],
                session["creature"],
                session["name"],
            )
        )
        parsed_response = parser(response.text)
        title = parsed_response[0]
        body = parsed_response[1]
        choice1 = parsed_response[2][0]
        choice2 = parsed_response[2][1]
        choice3 = parsed_response[2][2]
        choice4 = parsed_response[2][3]

        return render_template(
            "game.html",
            title_head=title[0],
            title_desc=title[1],
            body=body,
            choice1=choice1,
            choice2=choice2,
            choice3=choice3,
            choice4=choice4,
        )

    if request.method == "POST":
        response = CHAT.send_message(
            chapter_prompt(
                "1",  # chapter_num,
                "1",  # choice,
                session["story_length"],
                100,  # random
            )
        )
        parsed_response = parser(response.text)
        title = parsed_response[0]
        body = parsed_response[1]
        choice1 = parsed_response[2][0]
        choice2 = parsed_response[2][1]
        choice3 = parsed_response[2][2]
        choice4 = parsed_response[2][3]
        return render_template(
            "game.html",
            title_head=title[0],
            title_desc=title[1],
            body=body,
            choice1=choice1,
            choice2=choice2,
            choice3=choice3,
            choice4=choice4,
        )


@app.route("/refresh", methods=["POST"])
def refresh():
    """
    Refreshes page so that the player can generate more content
    """
    return redirect(url_for("game"))
