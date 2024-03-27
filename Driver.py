import prompt_engineering as pe
import random
print("Write the first chapter (out of ***story_length*** chapters) of a choose-your-own-adventure story about ***theme***, written in ***person_type*** person, that ends with a choice for the user to make. The choice should have between 2 and 4 options. The protagonist should be ***creature*** named ***name***.")
story_length = int(input("How long (how many pages)? "))
theme = input("Choose a theme (i.e. pirates, space adventure, etc.)? ")
perspective = input("What perspective, first or third? ")
creature = input("What creature do you want to play as? (elf, bear, human, etc) ")
name = input("What's your name adveturer? ")

response = pe.chat.send_message(pe.intro_prompt(story_length, theme, perspective, creature, name))
print(response.text)
user_choice = int(input("What's your choice: 1, 2, 3, or 4? "))


for i in range(story_length):
    if i != 0 or i != 1:
        rand = random.randint(0,10)
        print(rand)
        #model = pe.chapter_prompt(chapter_num= i, choice= user_choice, title= title, body= body)
        #model_output, title, body = p.parser(model)
        response = pe.chat.send_message(pe.chapter_prompt(chapter_num= i, choice= user_choice, story_length= story_length, random=rand))
        print(response.text)
        user_choice = int(input("What's your choice: 1, 2, 3, or 4? "))
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")

response = pe.chat.send_message(pe.endding_prompt(choice= user_choice))
print(response.text)