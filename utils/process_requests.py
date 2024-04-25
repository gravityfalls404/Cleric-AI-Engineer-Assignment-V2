from uuid import uuid4
import queue
import time
import requests
from utils.cache import Cache

cache = Cache()

class Requests:
    def __init__(self, question, documents_urls):
        self.question = question
        self.docs_urls = documents_urls
        self.status = "processing"
        self.request_id = str(uuid4())
        self.docs = self.get_docs_from_urls(documents_urls)
        self.response = None
    
    def read_text_from_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                text_content = response.text
                return text_content
            else:
                print(f"Error: HTTP status code {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
        
    def get_docs_from_urls(self, urls):
        docs = []
        for url in urls:
            docs.append(self.read_text_from_url(url))
        return docs

class RequestHandler:
    def __init__(self):
        self.requests_queue = queue.Queue()
        self.responses_queue = queue.Queue()
        self.current_question = None

    def add_request_to_request_queue(self, ques, docs_urls):
        request = Requests(ques, docs_urls)
        self.requests_queue.put(request)
    
    def add_request_to_response_queue(self, request):
        self.responses_queue.put(request)
    
    def get_from_request_queue(self):
        request = self.requests_queue.get(timeout=1)
        return request
    
    def get_from_response_queue(self):
        if self.responses_queue.empty():
            return
        
        response = self.responses_queue.get(timeout=1)
        return response

    
    def process_request(self):
        while True:
            try:
                request = self.get_from_request_queue()
                self.current_question = request.question
                processed_request = cache.get_cached_responses(request)
                self.add_request_to_response_queue(processed_request)
            except queue.Empty:
                time.sleep(0.1)

        

    
    
    

