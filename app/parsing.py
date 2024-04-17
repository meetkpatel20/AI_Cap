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


def parse_ending(response):
    text = response.split("###")
    title, body = text[1], text[2]

    title = title.strip().split(": ")
    title[0] = int(title[0][8:10])
    body = body.strip()

    return (title, body)


class Response():
    def __init__(self, response):
        self.text = self.parse(response.text)
        self.title = self.text[0]
        self.body = self.text[1]
        self.choices = self.text[2]
        self.choice1 = self.choices[0]
        self.choice2 = self.choices[1]
        self.choice3 = self.choices[2]
        self.choice4 = self.choices[3]

    def parse(self, response):
        text = response.split("###")
        title, body, choices = text[1], text[2], text[4]

        title = title.strip().split(": ")
        title[0] = int(title[0][8:10])
        body = body.strip()
        choices = choices.strip()

        choices = choices.split("\n")
        for i in range(len(choices)):
            choices[i] = choice_parsing(choices[i])

        return (title, body, choices)
