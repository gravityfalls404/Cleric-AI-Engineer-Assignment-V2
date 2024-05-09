import queue

class ResponseHandler():
    """
        Class consisting of methods for responding to the response api calls.
        The class is responsible for adding requests to the response queue,
        popping requests from the response queue and checking if the response is ready.
    """
    def __init__(self):
        self.response_queue = queue.Queue()

    def add_to_response_queue(self, request):
        self.response_queue.put(request)
    
    def pop_from_response_queue(self):
        request =  self.response_queue.get()
        request.response = request.celery_task.get()
        return request
    
    def peep_from_response_queue(self):
        copy = self.response_queue.queue
        if len(copy) == 0:
            return False, None
        top_request = copy[0]
        return top_request.celery_task.ready(), top_request.question

