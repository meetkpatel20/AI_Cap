import prompt_engineering as pe
import random
print("Write the first chapter (out of ***story_length*** chapters) of a choose-your-own-adventure story about ***theme***, written in ***person_type*** person. The protagonist should be ***creature*** named ***name***.\n")

val = True
while val == True:
    try:  
        story_length = int(input("How long (how many pages)? \n"))
        theme = input("Choose a theme (i.e. pirates, space adventure, etc.)? \n")
        perspective = input("What perspective, first or third? \n")
        creature = input("What creature do you want to play as? (elf, bear, human, etc) \n")
        name = input("What's your name adveturer? \n")
        val = False
    except:
        print("please re-enter a number")

response = pe.chat.send_message(pe.intro_prompt(story_length, theme, perspective, creature, name))
print(response.text)
val = True
while val == True:
    try:   
        user_choice = int(input("What's your choice: 1, 2, 3, or 4? "))
        val = False
    except:
        print("please re-enter a number")


for i in range(story_length):
    if i != 0 or i != 1:
        rand = random.randint(0,10)
        print(rand)
        #model = pe.chapter_prompt(chapter_num= i, choice= user_choice, title= title, body= body)
        #model_output, title, body = p.parser(model)
        response = pe.chat.send_message(pe.chapter_prompt(chapter_num= i, choice= user_choice, story_length= story_length, random=rand))
        print(response.text)
        val = True
        while val == True:
            try:   
                user_choice = int(input("What's your choice: 1, 2, 3, or 4? "))
                val = False
            except:
                print("please re-enter a number")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")

response = pe.chat.send_message(pe.endding_prompt(choice= user_choice))
print(response.text)