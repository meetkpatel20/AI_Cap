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
from app.model_helpers import generate_chain, get_model_response

CHAIN = None
PARSER = None

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
    session["perspective"] = request.args.get("person-type")
    session["creature"] = request.args.get("creature")
    session["name"] = request.args.get("name")

    global CHAIN, PARSER
    CHAIN, PARSER = generate_chain(session)
    content = get_model_response(CHAIN, PARSER, session["current_chapter"], "None")

    return render_template(
        "begin.html",
        chapter_num=session["current_chapter"],
        title=content.get("title"),
        body=content.get("body"),
        # image_link = image_link
        choice1=content.get("choice1"),
        choice2=content.get("choice2"),
        choice3=content.get("choice3"),
        choice4=content.get("choice4"),
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
