from django.http import HttpResponse

def healthz_view(request):
    """A view that returns HTTP 200 response for health checks."""
    return HttpResponse('OK', status=200)