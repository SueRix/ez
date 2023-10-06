from django.http import HttpResponse

def view2(request):
    response_text = "Hello from second server!"
    return HttpResponse(response_text)