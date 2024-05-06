"""
Routes for game engine
"""
from openai import OpenAI
from flask import render_template, request, redirect, url_for, session

from app import app
from app.prompt_engineering import (
    create_system_message,
    create_intro_prompt,
    create_game_prompt,
    create_ending_prompt,
)
from app.parsing import parse_response
from app.model_helpers import add_message_to_history, send_message

client = OpenAI()
HISTORY = []


@app.route("/")
@app.route("/start")
def start():
    """
    starting page
    """
    session["current_chapter"] = 0

    return render_template("start.html")


@app.route("/begin", methods=["GET"])
def begin():
    """
    first game page
    """
    session["current_chapter"] += 1
    session["story_length"] = request.args.get("story-length")
    session["theme"] = request.args.get("theme")
    session["person_type"] = request.args.get("person-type")
    session["creature"] = request.args.get("creature")
    session["name"] = request.args.get("name")

    system_message = create_system_message(
        session["story_length"],
        session["theme"],
        session["person_type"],
        session["creature"],
        session["name"],
    )
    add_message_to_history(HISTORY, "system", system_message)

    message = send_message(HISTORY, create_intro_prompt())

    parsed_response = parse_response(message)

    title = parsed_response[0]
    body = parsed_response[1]
    image_prompt = parsed_response[2]
    choices = parsed_response[3:]

    # call image generation here

    return render_template(
        "begin.html",
        chapter_num=session["current_chapter"],
        title=title,
        body=body,
        # image_link = image_link
        choice1=choices[0],
        choice2=choices[1],
        choice3=choices[2],
        choice4=choices[3],
    )


@app.route("/game", methods=["POST"])
def game():
    """
    Game page
    """
    session["current_chapter"] += 1

    if session["current_chapter"] == int(session["story_length"]):
        return redirect(url_for("end"))

    message = send_message(
        HISTORY, create_game_prompt(session["current_chapter"], HISTORY[-1]["content"])
    )

    parsed_response = parse_response(message)
    print(parsed_response)

    title = parsed_response[0]
    body = parsed_response[1]
    image_prompt = parsed_response[2]
    choices = parsed_response[3:]

    # call image generation here

    return render_template(
        "game.html",
        chapter_num=session["current_chapter"],
        title=title,
        body=body,
        # image_link = image_link
        choice1=choices[0],
        choice2=choices[1],
        choice3=choices[2],
        choice4=choices[3],
    )


@app.route("/end", methods=["GET"])
def end():
    response = send_message(HISTORY, create_ending_prompt(HISTORY[-1]["content"]))
    parsed_response = parse_response(response)
    title = parsed_response[0]
    body = parsed_response[1]
    return render_template(
        "end.html",
        chapter_num=session["current_chapter"],
        title=title,
        body=body,
    )
