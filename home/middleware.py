# middleware.py
from django.http import HttpResponsePermanentRedirect

class EnforcePrimaryDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host != 'www.mentalhealthmatters.sbs':
            return HttpResponsePermanentRedirect(
                f"https://www.mentalhealthmatters.sbs{request.get_full_path()}"
            )
        return self.get_response(request)
