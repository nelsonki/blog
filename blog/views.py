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
    response = requests.get('https://parseapi.back4app.com/b4aconsulta', headers=headers)
    if response:
        data = response.json()
        print(data)
        return render(request, 'blog/post_list.html', {'posts':data})
    else:
        print('Error fetching data from Parse' )
        return HttpResponse(f'Error fetching data from Parse  ' , status=500)

 