def choice_parsing(choice):
    choice = choice[3:]         # get rid of choice number
    choice = choice.split("**")  # split into choice title and description
    # choice = choice[1:3]        # get rid of empty list element
    # choice[0] = choice[0][:-1]  # get rid of colon in title
    # choice[1] = choice[1][1:]   # get rid of space at beginning of description
    return "".join(choice[1:3])


def parser(response):
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
