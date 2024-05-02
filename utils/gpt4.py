import openai
from utils.requests import Requests
import os

class GPT4:
    def __init__(self):
        self.client = openai.Client(api_key=os.environ.get("OPENAI_API_KEY"))

    def parse_llm_response(self, response_from_llm):
        response_from_llm = list(filter(len, response_from_llm.split(".")))
        return response_from_llm


    def get_openai_response(self, request: Requests):
        prompt = open("prompt.txt", "r")
        prompt_text = prompt.read()
        docs = list()
        docs.append({"role": "system", "content": prompt_text + '\n' + request.question})
        _ = self.client.chat.completions.create(
            model="gpt-4",
            messages=docs
        )
        for doc in request.docs:
            docs.append({"role": "user", "content": doc})
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=docs
            )
        return response.choices[0].message.content

        
        
    def get_response_from_llm(self, request: Requests):
        response_from_llm = self.get_openai_response(request)
        parsed_llm_response = self.parse_llm_response(response_from_llm)
        return parsed_llm_response

