class Prompt:
    def __init__(self):
        self.format = """
        """
        self.breaker = "\n\n############################################\n\n"


FORMAT = """The response should be given in the following format:

### Story chapter and title ###
Give the chapter of the story here

### Options ###
1. ** Option 1 title ** Option 1 description (DO NOT LIST A CHAPTER TO GO TO)
2. ** Option 2 title ** Option 2 description (DO NOT LIST A CHAPTER TO GO TO)
...
n. ** Option n title ** Option n description (DO NOT LIST A CHAPTER TO GO TO)"""


ENDING_FORMAT = """The response should be given in the following format:

### Story chapter and title ###
Give the chapter of the story here

"""


BREAKER = "\n\n############################################\n\n"


def intro_prompt(story_length, theme, person_type, creature, name):
    """
    Generates the prompt for the first chapter of the story.

    Args:
        story_length (str): The number of chapters the story should reach (ex: "ten").
        theme (str): The theme of the story.
        person_type (str): The person type the story is written in (i.e. "first", "second", ...).
        creature (str): The creature the protagonist should be.
        name (str): The name of the protagonist.

    Returns:
        str: The prompt to send to the model.
    """
    instructions = f"""
        Write the first chapter (out of {story_length} chapters) of a choose-your-own-adventure story
        about {theme}, written in {person_type} person, that ends with a choice for the user to make.
        The choice should have 4 options. The protagonist should be {creature} named {name}.
    """

    return instructions + BREAKER + FORMAT


def chapter_prompt(chapter_num, choice, story_length, random):
    """
    Generates the prompt for chapters of the story excluding the first and last chapter.

    Args:
        chapter_num (str): The chapter number
        choice (str): The user's choice in the previous chapter in format "1. Title: Body"

    Returns:
        str: The prompt to send to the model.
    """
    instructions = f"""
        Write the {chapter_num} chapter (out of {story_length} chapters) of the choose-your-own-adventure story 
        after the user chose to do this action: {choice} 

        Base your response on the previous history.

        The story should have possibilty of {random} out of 10 in terms of twists or negative consequences for a choice.

        The chapter should end in a choice for the user to make. The choice should have 4 options.
    """

    return instructions + BREAKER + FORMAT


def ending_prompt(choice):
    """
    Generates the prompt for the final chapter of the story.

    Arg:
        choice (str): The user's choice in the previous chapter in format "1. Title: Body"

    Returns:
        str: The prompt to send to the model.
    """
    instructions = f"""
        Write the final chapter of the choose-your-own-adventure story after the user chose to do this action: {choice} 

        Base your response on the previous history.

        The chapter should end with no choices for the user to make."""

    return instructions + BREAKER + ENDING_FORMAT 


# Sentiment Analysis prompt ------------------------------------------------------------------------
# input: sentiment, str -> the sentiment the model should use to analyze the user's choices in the
#                          story thus far (e.g., "safe" or "optimistic")
#        story, str     -> entire story thus far, including the chapter titles, bodies, and choices
#                          offered, and the choices made
# output: p3, str       -> the prompt to send to the model. Includes the instructions for the model
#                          on what to do and the format for the model's response
def sentiment_analysis(sentiment, story):
    p3 = f"""Generate a sentiment analysis for the choices made in the choose-your-own adventure story below.
  The response should be a single number on a scale from 1-100 based on how {sentiment} the
  choice is, with 100 being the most {sentiment}, and 1 being the least.

  Story:
  {story}"""
    return p3
