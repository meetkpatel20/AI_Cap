def choice_parsing(choice):
    """
    Breaks up the list of choices

    Args:
        choice (str)

    Returns
        list
    """
    choice = choice[3:]  # get rid of choice number
    choice = choice.split("**")  # split into choice title and description
    return "".join(choice[1:3])


def parse(response):
    """ """
    text = response.split("###")
    title, body, choices = text[1], text[2], text[4]

    title = title.strip().split(": ")
    title[0] = int(title[0][8:10])
    body = body.strip()
    choices = choices.strip()

    # parsing choices
    choices = choices.split("\n")
    for i in range(len(choices)):
        choices[i] = choice_parsing(choices[i])

    return (title, body, choices)
