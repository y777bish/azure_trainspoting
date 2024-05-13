import requests
from flask import Flask

limit = 3
api_url = 'https://api.api-ninjas.com/v1/dadjokes'
response = requests.get(api_url, headers={'X-Api-Key': 'ZZT6Fzqa7KEuHUeX5fCJZA==VaBqho2cDOOVtlew'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)

# Definiujemy trasę do strony głównej
@app.route('/')
def hello():
    return f'{response.json()[0]["joke"]}'

# Uruchamiamy serwer
if __name__ == '__main__':
    app.run()