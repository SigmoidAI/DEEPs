import time
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {
      "role": "system",
      "content": ""
    }
  ]


def set_system_role(content):
    messages[0]['content'] = content


def restart_chat():
    global messages
    messages = [
        {
            "role": "system",
            "content": ""
        }
    ]


def get_response_gpt(question, temperature=0):
    global messages

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature,
        max_tokens=5000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    messages.append(dict(response['choices'][0]['message']))
    return response['choices'][0]['message']['content']


def generate_response(
    prompt_input: str,
    setting: str = 'You are a biomedical research expert'
):
    """
    This function will take the prompt input and generate a response

    Args:
        prompt_input (str): The prompt input from the user

    Returns:
        the_answer (dict): The answer from the model

    """

    documents = ["http://www.ncbi.nlm.nih.gov/pubmed/21618594",
                 "http://www.ncbi.nlm.nih.gov/pubmed/23698708"]

    set_system_role(setting)
    response = get_response_gpt(prompt_input)

    response = 'By synthesizing the information from the documents, we found following information: \n\n ' + \
        response + '.' + '\n\n' + 'The documents we used to create this response are: '

    return response, list(set(documents))



def get_final_message(text,question):

    '''
    This function retreives the abstract paragraphs from WiseCube API and the question and returns the final message.

    Args: 

        text : (str) "abstract" type paragraphs, divided by the "\n".

        question: (str) just the question.

    Returns:

        result_text: (str) returns the final message.
    '''

    prompt = f'''"text":"{text}"

    You have the text above with the "text" tag. These are fragments of articles related with each other by a topic and each article is divided by the \n symbol. Based on these articles, 
    resume the information and give a impecable response. Keep in mind that you have 2 main parameters: "user" - role of the user, and "question", the question to which this 
    articles are related and to which you need to answer. Also, make sure to just directly answer, without stating the text this is coming from or any other side details. 
    "user": biomedical researcher
    "question": "{question}"'''

    messages=[
        {
        "role": "system",
        "content": "Biotech specialist"
        },
        {
        "role": "user",
        "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0,
    max_tokens=5000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    result_text = response['choices'][0]['message']['content']

    return result_text





