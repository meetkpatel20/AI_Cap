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

# input: model_output, str -> the whole model output for any particular
#                             besides the last chapter, containing the chapter
#                             title, the body of the chapter, and the choices
#                             for the user to make
# output: title, list      -> a list where the first element is a number
#                             labeling the chapter in question and the second
#                             is a str containing the chapter title
#         body, str        -> a str of the body of the chapter, including new
#                             line breaks for paragraphs
#         choices, list    -> a list with 4 elements, where each element is a
#                             list containing data for a particular choice the
#                             user can make. Each smaller list contains 2
#                             elements, the first being the tile of the choice
#                             and the second being a description of the choice
def parse(model_output):
    text = model_output.split("###")
    title, body, choices  = text[1], text[2], text[4]

    title = title.strip().split(": ")
    title[0] = int(title[0][8:10])
    body = body.strip()
    choices = choices.strip()

    # parsing choices
    choices = choices.split("\n")
    for i in range(len(choices)):
        choices[i] = choiceParsing(choices[i])
    return title, body, choices

model_output_test = """### Chapter 1: The Desolate Dawn ###

Frank, the lone amoeba, emerged from the depths of a nuclear wasteland. The once-vibrant world had been reduced to ruins, leaving behind only barren landscapes and toxic remains.

Frank had witnessed the cataclysmic event that had wiped out civilization, and he had endured the harsh aftermath, feeding on the microscopic remnants of the once-teeming biosphere. Now, as the sun peeked through the desolate horizon, he found himself at a crossroads.

### Options ###

1. **Venture into the Unknown:** Move towards the unfamiliar, where unknown dangers and potential opportunities await.
2. **Search for Shelter:** Seek refuge in a nearby abandoned structure, hoping to find safety and sustenance within its crumbling walls.
3. **Follow the Glow:** Notice a faint shimmer in the distance, suggesting the presence of something different or perhaps a sign of life.
4. **Wait and Observe:** Remain in place, keeping a watchful eye on the surroundings, awaiting any sign of movement or opportunity."""

title, body, choices = parse(model_output_test)

print("Title: ", title, "\n")
print("Body: " + body + "\n")
print("Choice 1:", choices[0], "\n")
print("Choice 2:", choices[1], "\n")
print("Choice 3:", choices[2], "\n")
print("Choice 4:", choices[3])
