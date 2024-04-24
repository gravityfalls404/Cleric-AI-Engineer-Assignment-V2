import hashlib
from gpt4 import get_openai_response


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

    def get_cached_responses(self, question, urls):
        # Generate the cache key based on the question and URLs
        cache_key = self.generate_cache_key(question, urls)

        # Check if the cache key exists in the cache
        if cache_key in self.cache:
            print("Cache hit!")
            return self.cache[cache_key]
        else:
            print("Cache miss!")

            # Fetch responses from OpenAI for each URL
            responses = "dummy responses" ## TODO: fetch responses from openai server.

            # Store the responses in the cache
            self.cache[cache_key] = responses
            return responses