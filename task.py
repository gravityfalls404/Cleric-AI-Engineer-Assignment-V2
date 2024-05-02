from celery import Celery
from utils import Cache, Requests, GPT4
import os

celery = Celery('task', broker=os.environ.get("REDIS_URL"), backend=os.environ.get("REDIS_URL"))

RESPONSE_QUEUE = list()
cache = Cache()
gpt4 = GPT4()

@celery.task
def process_request(ques, docs_url):
    ### Check if the request hashkey already exists cache.
    ### If exists return the response from cache.
    ### else process the request and add the response to cache. Processing involves using get_response_from_llm method of GPT4 class.
    request = Requests(ques, docs_url)
    response = cache.get_cached_responses(request)
    if response:
        return response
    response = gpt4.get_response_from_llm(request)
    cache.add_to_cache(request, response)
    return response
   