import parsing as p
import prompt_engineering as pe

f = open('history.txt', 'w')
f.write("")
f.close

story_length = int(input("How long (how many pages)?"))
theme = input("Choose a theme (i.e. pirates, space adventure, etc.)?")
perspective = input("What perspective, first or third")
creature = input("What creature do you want to play as? (elf, bear, human, etc)")
name = input("What's your name adveturer?")
#user_choice = input("What's your choice?")
model = pe.m1("first", story_length, theme, perspective, creature, name)
model_output = p.parser(model)

for i in range(story_length):
    if i != 0 or i != 1:
        model = pe.m1(i, story_length, theme, perspective, creature, name)
        model_output = p.parser(model)