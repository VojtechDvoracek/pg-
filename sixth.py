import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    odkazu a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Chyba pri stahovani url: {response.status_code}")

    content = response.text
    hrefs = []

    odkazy = content.split('href="')
    for odkaz in odkazy[1:]:
        href = odkaz.split('"')[0]
        if href.startswith("http"):
            hrefs.append(href)
    for href in hrefs:
        print(f"Odkaz: {href}")
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)

    except IndexError:
        print("Nebyla zadana URL.")

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
