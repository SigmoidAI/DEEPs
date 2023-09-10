import time
import os
import openai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

sessions = []

messages = [
    {
      "role": "system",
      "content": ""
    }
  ]

sessions.append(messages.copy())


def set_system_role(content):
    global sessions

    sessions[int(st.session_state.current_conversation.split('_')[1])-1][0]['content'] = content


def restart_chat():
    global messages
    messages = [
        {
            "role": "system",
            "content": ""
        }
    ]


def get_response_gpt(question, temperature=0):
    global sessions

    sessions[int(st.session_state.current_conversation.split('_')[1])-1].append(
        {
            "role": "user",
            "content": question
        }
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=sessions[int(st.session_state.current_conversation.split('_')[1])-1],
        temperature=temperature,
        max_tokens=7000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    sessions[int(st.session_state.current_conversation.split('_')[1])-1].append(dict(response['choices'][0]['message']))
    return response['choices'][0]['message']['content']


def generate_response(
    prompt_input: str,
):
    """
    This function will take the prompt input and generate a response

    Args:
        prompt_input (str): The prompt input from the user

    Returns:
        the_answer (dict): The answer from the model

    """




    return response



def get_final_message(text,question, setting='You are a Biotech specialist'):

    '''
    This function retreives the abstract paragraphs from WiseCube API and the question and returns the final message.

    Args: 

        text : (str) "abstract" type paragraphs, divided by the "\n".

        question: (str) just the question.

    Returns:

        result_text: (str) returns the final message.
    '''

    global messages

    if len(sessions) < int(st.session_state.current_conversation.split('_')[1]):
        sessions.append(messages.copy())

    prompt = f'''"text":"{text}"

    You have the text above with the "text" tag. These are fragments of articles related with each other by a topic and each article is divided by the \n symbol. Based on these articles, 
    resume the information and give a impecable response. Keep in mind that you have 2 main parameters: "user" - role of the user, and "question", the question to which this 
    articles are related and to which you need to answer. Also, make sure to just directly answer, without stating the text this is coming from or any other side details. 
    "user": biomedical researcher
    "question": "{question}"'''

    # messages=[
    #     {
    #     "role": "system",
    #     "content": "Biotech specialist"
    #     },
    #     {
    #     "role": "user",
    #     "content": prompt
    #     }
    # ]

    # response = openai.ChatCompletion.create(
    # model="gpt-4",
    # messages=messages,
    # temperature=0,
    # max_tokens=5000,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
    # )

    set_system_role(setting)
    response = get_response_gpt(prompt)  #'eduard te iubesc' + prompt_input #

    response = 'By synthesizing the information from the documents, we found following information: \n\n ' + \
        response + '.' + '\n\n' + 'The documents we used to create this response are: '

    return response





