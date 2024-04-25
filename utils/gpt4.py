import openai
from utils.requests import Requests
import time
from utils import cache

class GPT4:
    def __init__(self):
        pass

    def parse_llm_response(self, response_from_llm):
        response_from_llm.split(".")
        return response_from_llm


    def get_openai_response(self, request: Requests):
        ### Method to query Gpt4 using OpenAI API.
        time.sleep(5)
        return "dummy_response"
        
    def get_response_from_llm(self, request: Requests):
        ### Create a prompt by combining the question and the list of documents.
        ### Using the prompt and the documents one at a time get the final response from OpenAI.
        ### Parse and return the response.
        # prompt = f"I'm going to give you a list of call logs and along with that a question related to what the team has decided based on the logs. Give response in bullet points. Q: {reqquestion}\nDocuments:\n" + '\n'.join(documents)

        response_from_llm = self.get_openai_response(request)
        parsed_llm_response = self.parse_llm_response(response_from_llm)
        return parsed_llm_response

