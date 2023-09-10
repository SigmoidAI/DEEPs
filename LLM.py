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

    return text_variable, formatted_info


def send_to_front(usersearch):
    text_variable, formatted_info = extract_information(usersearch)
    message = get_final_message(text_variable,usersearch)
    return {'message': message, 'links': formatted_info}
