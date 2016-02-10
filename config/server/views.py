from django.http import HttpResponse

# Create your views here.


def show_start_page(request):
    return HttpResponse('Hello')
