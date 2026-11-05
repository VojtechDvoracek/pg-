import requests
import json
import sys

url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'

def get_model_names(prefix):
    responce= requests.get(url1+prefix)
    json_data = json.loads(responce.text)
    models = []
    for model in json_data["models"]:
        if model["name"].startswith(prefix):
            models.append(model["name"])
    return models

def download_rates():
    data = requests.get(url2)
    vysledek={}
    skip_lines = 2
    lines = data.text.splitlines()[skip_lines:]
    for line in lines:
        parts = line.split("|")
        rate = float(parts[4].replace(',', '.')) / int(parts[2])
        vysledek[parts[3]] = rate
    return vysledek
if __name__ == "__main__":
    # responce = requests.get(url)
    # if responce.status_code == 200:
    #     print(responce.content)
    #     responce.json()
    # if len(sys.argv) < 2:
    #     print(f"Usage: {sys.argv[0]} prefix")
    #     sys.exit()

    # prefix = sys.argv[1]
    # models = get_model_names(prefix)
    # for model in models:
    #    print(model)
    print(download_rates())