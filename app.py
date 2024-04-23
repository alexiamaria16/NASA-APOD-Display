from flask import Flask, render_template
import requests

# Creează o instanță Flask
app = Flask(__name__)

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

# Rulează aplicația
if __name__ == "__main__":
    app.run(debug=True)
