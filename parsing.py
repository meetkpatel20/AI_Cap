def choiceParsing(choice):
    choice = choice[3:]         # get rid of choice number
    choice = choice.split("**") # split into choice title and description
    choice = choice[1:3]        # get rid of empty list element
    choice[0] = choice[0][:-1]  # get rid of colon in title
    choice[1] = choice[1][1:]   # get rid of space at beginning of description
    return choice

def parser(model):
    text = model.split("###")
    title, body, choices  = text[1], text[2], text[4]

    title = title.strip().split(": ")
    title[0] = int(title[0][8:10])
    body = body.strip()
    choices = choices.strip()

    # parsing choices
    choices = choices.split("\n")
    for i in range(len(choices)):
        choices[i] = choiceParsing(choices[i])

    print("Title: ", title[1], "\n")
    print("Body: " + body + "\n")
    print("Choice 1:", choices[0], "\n")
    print("Choice 2:", choices[1], "\n")
    print("Choice 3:", choices[2], "\n")
    print("Choice 4:", choices[3])
    choice = int(input("What's your choice: 1, 2, 3, or 4?"))
    return(choices[choice-1], title, body)