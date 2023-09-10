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
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    sessions[int(st.session_state.current_conversation.split('_')[1])-1].append(dict(response['choices'][0]['message']))
    return response['choices'][0]['message']['content']

def intent_detection(question,temperature=0):
    global sessions

    current_messages = sessions[int(st.session_state.current_conversation.split('_')[1])-1].copy()
    current_messages.append(
        {
            "role": "user",
            "content": f'I have this question: {question}. Your task is to classify the question into one of the following categories: "research",\
              "general".The "research" tag will be about questions about biotech, medicine, and research purposes, and the "general" ones are presumably\
                about usual questions like "how are you?" or other general questions not related to biology,chemistry,biotech or biochemistry or medicine. As a response return only one word, the tag'

            # "content": f'I have this question: {question}. Tell me "research" if users questions is about research, and "general" if it is not about research'
        }
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=current_messages,
        temperature=temperature,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']['content']

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

    intent = intent_detection(question)

    if intent == 'general':
        prompt = 'Please give me an answer for the following question: ' + question
    else:
        prompt = f'''
        "text":"{text}"

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

    # if question.lower() == 'what is cancer?':
    #     response = 'cancer is a significant global health issue with increasing incidence and mortality rates. The "Cancer statistics, 2020" paper provides a comprehensive overview of the most recent data on cancer incidence, mortality, and survival in the United States. It highlights that the cancer death rate has been steadily declining in the U.S., but there is still a significant burden of cancer in the country. The "Global cancer statistics 2018: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries" paper provides a global perspective on cancer. It presents estimates of the incidence and mortality of 36 types of cancer in 185 countries. The paper highlights that the global cancer burden is significant and is expected to increase due to the growth and aging of the population.'
    # elif question.lower() == 'what is the most common cancer?':
    #     response = 


    # ['https://www.nature.com/articles/s41592-018-0260-3',
    #  ]
    # time.sleep(3)
    set_system_role(setting)
    response = get_response_gpt(prompt)  #'eduard te iubesc' + prompt_input #

    if intent == 'research':
        response = 'By synthesizing the information from the documents, we found following information: \n\n ' + \
            response + '.' + '\n\n' + 'The documents we used to create this response are: '

    return response, intent
