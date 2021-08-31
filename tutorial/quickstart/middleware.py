import time
from django.utils.deprecation import MiddlewareMixin


class RequestTimeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.META['TIME'] = time.monotonic()

    def process_response(self, request, response):
        delta_timing = (time.monotonic() - request.META['TIME']) * 100000
        total_timing = f"{int(delta_timing)}ms"
        response.headers['X-Request-Timing'] = total_timing

        return response
