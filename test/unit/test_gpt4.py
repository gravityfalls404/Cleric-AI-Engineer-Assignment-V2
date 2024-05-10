from unittest import TestCase
from unittest.mock import patch
from utils import GPT4, Requests
from utils import gpt4

class TestGPT4(TestCase):
    @patch('utils.gpt4.GPT4.get_openai_response')  
    def test_get_response_from_llm(self, mock_fetch):
        gpt_client = GPT4()
        mock_fetch.return_value = "Lorem ipsum dolor sit amet, consectetur adip. Lorem ipsum dolor sit amet, consectetur adip."
        
        random_ques = "Lorem ipsum dolor sit amet, consectetur adip"
        ranodm_request = Requests(random_ques, ['a', 'b', 'c', 'd', 'e', 'f'])
        response = gpt_client.get_response_from_llm(ranodm_request)
        assert response == ["Lorem ipsum dolor sit amet, consectetur adip", "Lorem ipsum dolor sit amet, consectetur adip"]


            
            
