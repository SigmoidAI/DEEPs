import time

def process_llm_output(
    the_answer: dict,
):
    """
    This function will process the output dictionary output of the model to combine the text and the 
    links in an appropriate way to be displayed to the user.

    Args:
        the_answer (dict): The answer from the model

    Returns:
        main_text (str): The main text of the answer
        links (list): The unique links of the answer 
        
    """
    main_text = the_answer["message"]
    links = the_answer["links"]
    return main_text, list(set(links))


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
    # some dark magic should happen here
    # and a function will do something about the prompt aferwards generating the response
    # in an answer variable that will be returned
    the_answer = {
        "message": f"{prompt_input} - This is the output the message that will contain the main idea of the project{prompt_input}",
        "links": ["https://www.google.com", "https://doogle.com", "https://www.googcom"]
    }
    return process_llm_output(the_answer)
