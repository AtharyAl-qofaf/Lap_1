import time

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = (time.time() - start_time) * 1000  # الحساب بالملي ثانية
        response['X-Response-Time-ms'] = f"{duration:.2f}ms"
        return response