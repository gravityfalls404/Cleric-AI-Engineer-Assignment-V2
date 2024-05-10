from utils import Cache, Requests
class TestCache():
    def test_caching(self):
        self.cache = Cache()
        random_ques = "Lorem ipsum dolor sit amet, consectetur adip"
        random_response = "Lorem ipsum dolor sit amet, consectetur adip"
        ranodm_request = Requests(random_ques, ['a', 'b', 'c', 'd', 'e', 'f'])
        self.cache.add_to_cache(ranodm_request, random_response)
        assert self.cache.get_cached_responses(ranodm_request) != None
    
    def test_generate_cache_key(self):
        self.cache = Cache()
        random_ques = "Lorem ipsum dolor sit amet, consectetur adip"
        ranodm_request = Requests(random_ques, ['a', 'b', 'c', 'd', 'e', 'f'])
        cache_key = self.cache.generate_cache_key(ranodm_request)
        cache_key_2 = self.cache.generate_cache_key(ranodm_request)

        assert cache_key == cache_key_2