from django.shortcuts import render
from .models import Post
from django.utils import timezone
import requests
from django.conf import settings
from django.http import HttpResponse

def post_list(request):
    headers = {
        'X-Parse-Application-Id': settings.PARSE_APP_ID,
        'X-Parse-REST-API-Key': settings.PARSE_REST_API_KEY,     
    }
    response = requests.get('https://parseapi.back4app.com/classes/b4aconsulta', headers=headers)
    if response.status_code == 200:
        posts = response.json()
        return render(request, 'blog/post_list.html', {'posts':posts['results']})
    else:
        error_message = response.text  # El texto del error proporcionado por la API de Parse
        print('Error fetching data from Parse: ', error_message)
        return HttpResponse(f'Error fetching data from Parse: {error_message}', status=500)

    