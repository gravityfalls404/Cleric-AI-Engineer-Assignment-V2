from uuid import uuid4
from gpt4 import get_openai_response
import queue

class Requests:
    def __init__(self):
        self.questions = None
        self.documents_urls = []
        self.status = "processing"
        self.request_id = str(uuid4())

class RequestHandler:
    def __init__(self):
        self.requests_queue = queue.Queue()
        self.responses_queue = queue.Queue()
        self.current_question = None

    def add_request(self, request):
        self.requests_queue.append(request)
    
    def add_response(self, response):
        self.responses_queue.append(response)
    
    def process_request(self):
        pass
    
    def get_from_response_queue(self):
        if self.responses_queue.empty():
            return
        
        response = self.responses_queue.get()
        return response

        

    
    
    

