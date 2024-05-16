from django.shortcuts import render
from .models import Post
from django.utils import timezone
import requests
from django.conf import settings
from django.http import HttpResponse

def post_list(request):
    headers = {
        'X-Parse-Application-Id': 'BIKe377T64cE2OyCZIiExRu5hqxV8DkS5AH7rJfN',
        'X-Parse-REST-API-Key': '1ypPpH7UqrqkekilT2UXvGwElXPXMcrle9JLSvKB',     
    }
    response = requests.get('https://parseapi.back4app.com/classes/Consulta', headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request, 'blog/post_list.html', {'posts':data})
    else:
        error_message = response.text  # El texto del error proporcionado por la API de Parse
        print('Error fetching data from Parse: ', error_message)
        return HttpResponse(f'Error fetching data from Parse: {error_message}', status=500)

    