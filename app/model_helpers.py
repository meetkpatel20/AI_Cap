from openai import OpenAI

client = OpenAI()


def add_message_to_history(history, role, message):
    history.append({"role": role, "content": message})


def send_message(history, prompt):
    add_message_to_history(history, "user", prompt)
    response = client.chat.completions.create(
        messages=history,
        model="gpt-3.5-turbo",
        frequency_penalty=0.8,
        presence_penalty=0.8,
        temperature=0,
    )
    message = response.choices[0].message.content
    add_message_to_history(history, "assistant", message)
    return message
