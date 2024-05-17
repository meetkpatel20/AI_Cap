from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper


def generate_output_parser(ending=False):
    response_schemas = []
    response_schemas.append(
        ResponseSchema(
            name="title",
            description="the chapter's title in the form 'ChapterNumber: Title'"
        )
    )
    response_schemas.append(
        ResponseSchema(
            name="body",
            description="the body of the chapter's content using 150 words"
        )
    )
    response_schemas.append(
        ResponseSchema(
            name="img_prompt",
            description="a summarization of the body used for image generation in less that 100 words but be sure to include descriptors about the character and setting",
        )
    )

    if not ending:
        response_schemas.append(
            ResponseSchema(
                name="choice1",
                description="the first potential choice a player can make using 20 words"
            )
        )
        response_schemas.append(
            ResponseSchema(
                name="choice2",
                description="the second potential choice a player can make using 20 words"
            ),
        )
        response_schemas.append(
            ResponseSchema(
                name="choice3",
                description="the third potential choice a player can make using 20 words"
            )
        )
        response_schemas.append(
            ResponseSchema(
                name="choice4",
                description="the fourth potential choice a player can make using 20 words"
            )
        )

    output_parser = StructuredOutputParser.from_response_schemas(
        response_schemas
    )
    return output_parser


def generate_format_instructions(output_parser):
    format_instructions = output_parser.get_format_instructions()
    return format_instructions


def generate_game_prompt(story_elements, format_instructions):
    prompt = PromptTemplate(
        template=(
            "You are going to create a choose your own adventure style game that "
            f"is {story_elements['story_length']} chapters long told from the "
            f"{story_elements['perspective']}-person narrative style. The story "
            f"has a theme of {story_elements['theme']} where the main character "
            f"is a {story_elements['creature']} named {story_elements['name']}. \n"
            "You will be provided with the current chapter number and the choice "
            "the player made from a previous chapter below. If {chapter_number} == "
            f"{story_elements['current_chapter']}, this means this is the last "
            "chapter and the body should be the story conclusion. Otherwise "
            "provide the user with the chapter body and four choices. If the "
            "previous choice is the word 'None', that means, this is the first "
            "chapter and there was no previous chapter. Otherwise base the story "
            "content on the previous choice the user made. Provide the player "
            "with four different choices they can make. Use about 200 words "
            "for all fields combined.\n"
            "{format_instructions}\n"
            "Chapter Number: {chapter_number}\n"
            "Previous Choice: {previous_choice}"
        ),
        input_variables=["chapter_number", "previous_choice"],
        partial_variables={"format_instructions": format_instructions},
    )
    return prompt


def generate_end_prompt(format_instructions):
    prompt = PromptTemplate(
        template=(
            "The game is almost over. Conclude the story with some ending "
            "based on the previous choice below. Do not generate new choices "
            "for this chapter.\n"
            "{format_instructions}\n"
            "Chapter Number: {chapter_number}\n"
            "Previous Choice: {previous_choice}"
        ),
        input_variables=["chapter_number", "previous_choice"],
        partial_variables={"format_instructions": format_instructions}
    )
    return prompt


def generate_chain(story_elements):
    output_parser = generate_output_parser()
    format_instructions = generate_format_instructions(output_parser)
    chain = LLMChain(
        llm=ChatOpenAI(),
        prompt=generate_game_prompt(story_elements, format_instructions),
        memory=ConversationSummaryMemory(
            llm=ChatOpenAI(), input_key="chapter_number"),
    )
    return chain, output_parser


def get_model_response(chain, parser, chapter_number, previous_choice):
    response = chain.invoke(
        {"chapter_number": chapter_number, "previous_choice": previous_choice}
    )
    content = parser.parse(response["text"])
    return content


def generate_image(content):
    print(content)
    img_url = DallEAPIWrapper().run(content)
    return img_url
