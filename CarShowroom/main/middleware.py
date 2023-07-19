from django.http import HttpResponseRedirect


class AdminIPRestrictionMiddleware:
    allowed_ips = ['192.168.1.53', '127.0.0.1', '192.168.0.104', '192.168.0.108', '192.168.1.62']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path == '/admin/' and request.META.get('REMOTE_ADDR') not in self.allowed_ips:
            return HttpResponseRedirect('/')

        response = self.get_response(request)
        return response
