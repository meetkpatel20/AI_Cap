def create_system_message(story_length, theme, person_type, creature, name):
    prompt = (
        f"You will be creating a choose your own adventure story that is {story_length} "
        f"chapters long where the theme is {theme}, the story is told in {person_type} "
        f"person narration, the main character is a {creature}, and the character's name "
        f"is {name}. The reponse should be in the following format: "
    )
    response_format = (
        "<h1>Insert chapter title here</h1>"
        "<p>Insert the chapter content here in less that 100 words</p>"
        "<p>Insert a brief sentence that summarizes the paragraph above</p>"
        "<ul>"
        "<li>Insert choice 1 here</li>"
        "<li>Insert choice 2 here</li>"
        "<li>Insert choice 3 here</li>"
        "<li>Insert choice 4 here</li>"
        "</ul>"
    )
    return prompt + response_format


def create_intro_prompt():
    prompt = "Create the first chapter of the story and provide 4 different choices."
    return prompt


def create_game_prompt(chapter_number, choice):
    prompt = (
        f"Create the chapter content for chapter {chapter_number} where the player "
        "made this choice: "
    )
    return prompt + choice


def create_ending_prompt(choice):
    prompt = (
        "Create the final chapter of the story where the player made this choice:"
        f"{choice}. Also disregard the previous response format and put the final response "
        "in this format: "
    )
    response_format = (
        "<h1>Insert chapter title here</h1>"
        "<p>Insert the chapter content here in less that 100 words</p>"
        "<p>Insert a brief sentence that summarizes the paragraph above</p>"
    )
    return prompt + response_format
