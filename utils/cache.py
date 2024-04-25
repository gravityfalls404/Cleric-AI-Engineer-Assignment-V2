import hashlib
from utils.gpt4 import get_openai_response


class Cache:
    def __init__(self):
        self.cache = {}

    def generate_cache_key(self, question, urls):
        # Create a unique hash key based on the question and list of URLs
        hash_key = hashlib.sha256()
        hash_key.update(question.encode('utf-8'))
        for url in urls:
            hash_key.update(url.encode('utf-8'))
        return hash_key.hexdigest()
    
    def parse_llm_response(self, response_from_llm): ##TODO
        response_from_llm.split(".")
        return response_from_llm

    def get_response_from_llm(self, request):
        response_from_llm = get_openai_response(request.question, request.docs)
        parsed_llm_response = self.parse_response(response_from_llm)
        return parsed_llm_response

    def get_cached_responses(self, request):
        # Generate the cache key based on the question and URLs
        cache_key = self.generate_cache_key(request.question, request.urls)

        # Check if the cache key exists in the cache
        if cache_key in self.cache:
            print("Cache hit!")
            return self.cache[cache_key]
        else:
            print("Cache miss!")

            # Fetch responses from OpenAI for each URL
            ## TODO: fetch responses from openai server. The request should be asynchronous.
            responses = self.get_response_from_llm(request)
            request.status = "done"
            request.response = responses

            # Store the responses in the cache
            self.cache[cache_key] = request
            return request