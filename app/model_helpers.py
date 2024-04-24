from openai import OpenAI

client = OpenAI()


def add_message_to_history(history, role, message):
    history.append({"role": role, "content": message})


def send_message(history, prompt):
    add_message_to_history(history, "user", prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
    )
    message = response.choices[0].message.content
    add_message_to_history(history, "assistant", message)
    return message
