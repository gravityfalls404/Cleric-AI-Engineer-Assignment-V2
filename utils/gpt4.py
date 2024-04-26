import openai
from utils.requests import Requests
import time
from constants import OPENAI_API_KEY

class GPT4:
    def __init__(self):
        self.client = openai.Client(api_key=OPENAI_API_KEY)

    def parse_llm_response(self, response_from_llm):
        response_from_llm.split(".")
        return response_from_llm


    def get_openai_response(self, request: Requests):
        ### This method will be used to query openai api.
        ### first it'll read the prompt from the prompt.txt file and send it to openai.
        ### then it'll use the request.docs which is a list of documents to send request to 
        ### the openai api one at a time. Final response from the api will be returned.
        ### The response from the api will be stored in the request object.
        ### The request object will be added to the RESPONSE_QUEUE.
        ### The RESPONSE_QUEUE will be used by the worker to process the requests.
        prompt = open("prompt.txt", "r")
        prompt_text = prompt.read()
        _ = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
        )
        docs = [request.question]
        for doc in request.docs:
            docs.append(doc)
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt = prompt_text,
                message=docs
            )
        return response.choices[0].text.strip()
        
        
    def get_response_from_llm(self, request: Requests):
        response_from_llm = self.get_openai_response(request)
        parsed_llm_response = self.parse_llm_response(response_from_llm)
        return parsed_llm_response

