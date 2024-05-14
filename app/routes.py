"""
Routes for game engine
"""
from flask import render_template, request, redirect, url_for, session
from app import app
from app.langchain_utils import (
    generate_chain,
    get_model_response,
    generate_end_prompt,
    generate_output_parser,
    generate_format_instructions,
    generate_image
)

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
    content = get_model_response(
        CHAIN, PARSER, session["current_chapter"], "None")
    session["body"] = content.get("body")
    img_url = generate_image(session["body"])

    return render_template(
        "begin.html",
        title=content.get("title"),
        body=content.get("body"),
        image_link=img_url,
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

    content = get_model_response(
        CHAIN, PARSER, session["current_chapter"], session["body"]
    )
    session["body"] = content.get("body")
    img_url = generate_image(session["body"])

    return render_template(
        "game.html",
        title=content.get("title"),
        body=content.get("body"),
        image_link=img_url,
        choice1=content.get("choice1"),
        choice2=content.get("choice2"),
        choice3=content.get("choice3"),
        choice4=content.get("choice4"),
    )


@app.route("/end", methods=["GET"])
def end():
    global CHAIN, PARSER
    PARSER = generate_output_parser(ending=True)
    format_instructions = generate_format_instructions(PARSER)
    prompt = generate_end_prompt(format_instructions)
    CHAIN.prompt = prompt
    content = get_model_response(
        CHAIN, PARSER, session["current_chapter"], session["body"]
    )
    img_url = generate_image(content.get("body"))

    return render_template(
        "end.html",
        title=content.get("title"),
        body=content.get("body"),
        image_link=img_url
    )
