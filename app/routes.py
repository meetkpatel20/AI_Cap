"""
Routes for game engine
"""
from flask import render_template, request, redirect, url_for
from app import app, call_gemini


@app.route('/')
@app.route('/start')
def start():
    """
    starting page
    """
    return render_template("start.html")


@app.route('/game', methods=['GET', 'POST'])
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
