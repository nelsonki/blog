from django.shortcuts import render
from .models import Post
from django.utils import timezone
import requests

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts':posts})
    def get_parse_data():
        headers = {
            'X-Parse-Application-Id': 'BIKe377T64cE2OyCZIiExRu5hqxV8DkS5AH7rJfN',  # Reemplazar con tu ID de aplicación de Parse
            'X-Parse-REST-API-Key': 'xhuEMTCuKKinvd28WbB2cz4pgUjQ2DKrtygeMqq4',      # Reemplazar con tu REST API Key de Parse
        }
    
        response = requests.get('https://parseapi.back4app.com/b4aconsulta', headers=headers)
    
        if response.status_code == 200:
            # Proceso exitoso, parsear y usar la data
            data = response.json()
            return data.get('results', [])
        else:
            # Manejar errores
            print('Error fetching data from Parse:', response.status_code, response.text)
            return None

    # Usar la función en tu vista o lógica de negocio
    objects = get_parse_data()  
    return render(request, 'blog/post_list.html', {'posts':objects})