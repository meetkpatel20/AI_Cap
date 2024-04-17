# FUNCTION ONLY USED IN PARSE FUNCTION, NOT DESIGNED FOR USE ELSEWHERE
# input: choice, str   -> the particular model output containing a singular
#                         choice from the list of choices a user can make in
#                         a chapter
# output: choice, list -> a list with 2 elements, the first being the tile of
#                         the choice, and the second being a description of
#                         the choice
def choiceParsing(choice):
    choice = choice[3:]         # get rid of choice number
    choice = choice.split("**") # split into choice title and description
    choice = choice[1:3]        # get rid of empty list element
    choice[0] = choice[0][:-1]  # get rid of colon in title
    choice[1] = choice[1][1:]   # get rid of space at beginning of description
    return choice

# this is the old parse function that was here when I copied my code in from
# the "jake" branch. It was a little different than my current one. It doesn't
# seem like my new version causes any issues, but in case it does, I wanted to
# keep the original
# def choice_parsing(choice):
#     """
#     Breaks up the list of choices

#     Args:
#         choice (str)

#     Returns
#         list
#     """
#     choice = choice[3:]  # get rid of choice number
#     choice = choice.split("**")  # split into choice title and description
#     return "".join(choice[1:3])


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
        choices[i] = choiceParsing(choices[i])
    
    return title, body, choices

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
# model_output_test = """### Chapter 1: The Desolate Dawn ###

# Frank, the lone amoeba, emerged from the depths of a nuclear wasteland. The once-vibrant world had been reduced to ruins, leaving behind only barren landscapes and toxic remains.

# Frank had witnessed the cataclysmic event that had wiped out civilization, and he had endured the harsh aftermath, feeding on the microscopic remnants of the once-teeming biosphere. Now, as the sun peeked through the desolate horizon, he found himself at a crossroads.

# ### Options ###

# 1. **Venture into the Unknown:** Move towards the unfamiliar, where unknown dangers and potential opportunities await.
# 2. **Search for Shelter:** Seek refuge in a nearby abandoned structure, hoping to find safety and sustenance within its crumbling walls.
# 3. **Follow the Glow:** Notice a faint shimmer in the distance, suggesting the presence of something different or perhaps a sign of life.
# 4. **Wait and Observe:** Remain in place, keeping a watchful eye on the surroundings, awaiting any sign of movement or opportunity."""
