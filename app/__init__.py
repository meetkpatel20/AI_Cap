"""
This app module puts the app into a module.
"""
from flask import Flask, session
import secrets

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = secrets.token_hex(16)
app.debug = True
