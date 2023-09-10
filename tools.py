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
    response = 'eduard te iubesc' #get_response_gpt(prompt_input)

    response = 'By synthesizing the information from the documents, we found following information: \n\n ' + \
        response + '.' + '\n\n' + 'The documents we used to create this response are: '

    return response, list(set(documents))
