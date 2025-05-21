# pipenv install beautifulsoup4
# pipenv shell
import requests
from bs4 import BeautifulSoup  # nos devuelve un string

url = "https://stackoverflow.com/questions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

preguntas = soup.select(".s-post-summary")

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"usuario {usuario.strip()} - Titulo: \n {titulo.strip()}")
    



