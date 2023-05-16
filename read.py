import requests
import dotenv
import os  

dotenv.load_dotenv(dotenv.find_dotenv())

apiKey = os.getenv("apiKey")
url = f'https://imdb-api.com/pt/API/Search/{apiKey}/MoonLight'

response = requests.get(url)

data = response.json()

id = data["results"][0]["id"]


urlRequest = f'https://imdb-api.com/pt/API/Title/{apiKey}/{id}'

responseNew = requests.get(urlRequest)

dataNew = responseNew.json()

##Nosso output

print(f'Nome do Filme: {dataNew["title"]} \n\nAno de lançamento: {dataNew["year"]}\n\nEstrelado por: {dataNew["stars"]}\n\nNota:{dataNew["imDbRating"]}\n\nPremios: {dataNew["awards"]}\n\nPlot:{dataNew["plotLocal"]}\n')