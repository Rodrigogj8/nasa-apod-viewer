import requests
import webbrowser
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv('API_KEY')

url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data['media_type'] == 'image':
        print(f'Data:{data["date"]}')
        print(f'Título: {data["title"]}')
        print(f'Descrição: {data["explanation"]}')
        print(f'Link da Imagem:{data["url"]}')
        webbrowser.open(data['url'])
else:
    print("Erro ao acessar a API da NASA.")