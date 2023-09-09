import time


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
    delay = 10
    time.sleep(delay)
    the_answer = {
        "message": f"This is the output the message that will contain the main idea of the project",
        "links": ["https://www.google.com", "https://www.google.com", "https://www.google.com"]
    }
    return the_answer


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
        links (list): The links of the answer
        
    """
    main_text = the_answer["message"]
    links = the_answer["links"]
    return main_text, links