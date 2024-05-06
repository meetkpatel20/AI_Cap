"""
Routes for game engine
"""
import google.generativeai as genai
import flask
#from flask import Flask, render_template, request, redirect, url_for

from app import constants
from app import app
#from app.prompt_engineering import chapter_prompt, ending_prompt, intro_prompt
from app.parsing import parser
import app.text_gen as gen

#genai.configure(api_key=constants.GOOGLE_API_KEY)
#CHAT = genai.GenerativeModel("gemini-pro").start_chat(history=[])

app = flask.Flask(__name__)
env = {}


@app.route("/test")
def teseter():
    """
    test page
    """
    return flask.render_template("test.html")

@app.route("/")
def start():
    """
    starting page
    """
    env["current_chapter"] = 0
    env["history"] = ""

    return flask.render_template("entry_form.html")


@app.route("/begin", methods=["GET"])
def begin():
    """
    first game page
    """
    env["current_chapter"] += 1
    env["story_length"] = flask.request.args.get("sl")
    env["theme"] = flask.request.args.get("story")
    env["person_type"] = flask.request.args.get("per")
    env["creature"] = flask.request.args.get("creature")
    env["name"] = flask.request.args.get("name")


    respo = gen.intro_prompt(env)

    response = gen.model(respo, env["history"])


    """
    response = CHAT.send_message(
        intro_prompt(
            env["story_length"],
            env["theme"],
            env["person_type"],
            env["creature"],
            env["name"],
        )
    )
    """
    parsed_response = parser(response)
    title = parsed_response[0]
    body = parsed_response[1]
    choice1 = parsed_response[2][0]
    choice2 = parsed_response[2][1]
    choice3 = parsed_response[2][2]
    choice4 = parsed_response[2][3]

    return flask.render_template(
        "begin.html",
        title_head=env["current_chapter"],
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
    env["current_chapter"] += 1

    if env["current_chapter"] == int(env["story_length"]):
        return flask.redirect(flask.url_for("end"))

    choice_made = flask.request.form["choice-btn"]
    response = CHAT.send_message(
        chapter_prompt(
            chapter_num=env["current_chapter"],
            story_length=env["story_length"],
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

    return flask.render_template(
        "game.html",
        title_head=env["current_chapter"],
        title_desc=title[1],
        body=body,
        choice1=choice1,
        choice2=choice2,
        choice3=choice3,
        choice4=choice4,
    )


@app.route("/end", methods=["GET"])
def end():
    choice_made = flask.request.args.get("choice-btn")
    response = CHAT.send_message(ending_prompt(choice_made))
    parsed_response = parse_ending(response.text)
    title = parsed_response[0]
    body = parsed_response[1]
    return flask.render_template(
        "end.html",
        title_head=env["current_chapter"],
        title_desc=title[1],
        body=body,
    )


# title = (100, "TESTING")
# body = "Lorem ipsum dolor sit amet, consectetur et est culpa et culpa duis."
# choice1 = "test"
# choice2 = "test test"
# choice3 = "test test test"
# choice4 = "test test test test"


if __name__ == '__main__':
    app.run(debug=True)