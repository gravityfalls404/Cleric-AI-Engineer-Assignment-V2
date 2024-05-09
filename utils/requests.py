from uuid import uuid4
import json
import requests

class Requests:
    """
        Class is a bluefprint of request entity with metadata about the request.
    """
    def __init__(self, question, documents_urls):
        self.question = question
        self.docs_urls = documents_urls
        self.status = "processing"
        self.celery_task = None
        self.docs = self.get_docs_from_urls(documents_urls)
        self.response = None
        
    def set_task(self, task):
        self.celery_task = task
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
    

