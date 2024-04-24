from flask import Flask, render_template
from flask_frozen import Freezer
import requests

#API KEY

API_KEY='M0Zjmh7ytaX52ThAE1kFbhZlui1bOsUhb3Q24Iav'

#API URL

url='GET https://api.nasa.gov/planetary/apod'


# Creează o instanță Flask
app = Flask(__name__)
freezer = Freezer(app)

# Definirea unei rute pentru pagină principală
@app.route("/")
def index():


    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

    if response.status_code == 200:
        data = response.json()

        image_url = data['url']
        title = data['title']
        explanation = data['explanation']
        
        return render_template('index.html', image_url=image_url, title=title, explanation=explanation)
    else:
        return 'Eroare la solicitarea API-ului NASA'

if __name__ == "__main__":
    freezer.freeze()