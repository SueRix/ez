import requests
from django.http import HttpResponse

def view1(request):
    try:
        response = requests.get('http://127.0.0.1:8080/view2/')

        if response.status_code == 200:
            response_text = "Привет от первого сервера!\nОтвет от второго сервера: " + response.text
        else:
            response_text = "Привет от первого сервера!\nОшибка при обращении к второму серверу"
    except requests.exceptions.RequestException as a:
        response_text = "Привет от первого сервера!\nОшибка при отправке запроса на второй сервер: " + str(a)

    return HttpResponse(response_text)