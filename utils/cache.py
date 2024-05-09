import hashlib
from utils.requests import Requests


class Cache:
    """
        Caching object. Check for the HASH code for the incoming requests and returns the stored
        response from the cache in case of cache hits. Else return None.
    """
    def __init__(self):
        self.cache = {}

    def generate_cache_key(self, request: Requests):
        hash_key = hashlib.sha256()
        hash_key.update(request.question.encode('utf-8'))
        for url in request.docs_urls:
            hash_key.update(url.encode('utf-8'))
        return hash_key.hexdigest()
    
    
    def get_cached_responses(self, request):
        cache_key = self.generate_cache_key(request)

        if cache_key in self.cache:
            return self.cache[cache_key]
        
        return
    
    def add_to_cache(self, request, response):
        cache_key = self.generate_cache_key(request)
        self.cache[cache_key] = response