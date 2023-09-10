from query_api import get_resources
from tools import get_final_message


def extract_information(usersearch):
    data = get_resources(usersearch)
    text_variable = ""
    formatted_info = []

    for title, info_list in data:
        for info_type, info_text in info_list:
            if info_type == 'abs':
                text_variable += info_text + '\n'
            elif info_type == 'source':
                formatted_info.append(f"{title}:{info_text}")

    # formatted_info = ['https://acsjournals.onlinelibrary.wiley.com/doi/full/10.3322/caac.21590', 
    #  'https://onlinelibrary.wiley.com/doi/full/10.3322/caac.21492',
    #  ]
    return text_variable, formatted_info


def send_to_front(usersearch):
    text_variable, formatted_info = extract_information(usersearch)
    message,intent = get_final_message(text_variable,usersearch)
    if intent == "research":
    # return {'message': message, 'links': formatted_info}
        return message, set(formatted_info)
    else: 
        return message, set()

