import google.generativeai as genai
from app import prompt, constants

# Text Method
genai.configure(api_key=constants.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
TEXT = ""


def generate_content():
    """
    Calls the Google Gemini API

    Return:
        string: API response
    """
    global TEXT
    TEXT += prompt.PROMPT

    response = model.generate_content(TEXT)
    parsed_response = parse_response(response.text)
    TEXT += parsed_response
    return parsed_response


def parse_response(response):
    """
    Parses the Gen AI response to extract a longer description and two options

    Args:
        response (string)

    Return:
        tuple: Contains the description and options in the form of (desc, opt1, opt2)
    """
    return response
