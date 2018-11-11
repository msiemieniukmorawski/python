import requests
import json
import os

current = "http://xkcd.com/info.0.json"
pattern = "https://xkcd.com/{num}/info.0.json"
json_data = None

folder = os.path.join(os.getcwd(), "comics")



def pobierz(link, sciezka):

    response = requests.get(link)

    if response.status_code == 200:

        bajty = 0

        try:
            with open(sciezka, 'wb') as plik:
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc
        except FileNotFoundError:
            # tutaj tworzymy foldery
            bajty = 99999

        print(f"Zapisano {bajty} bajtów")

def get_current_comic():
    global json_data
    response = requests.get(current)
    response.raise_for_status()

    json_data = json.loads(response.text, encoding="utf-8")

    with open("current.json", 'w') as plik:
        json.dump(json_data, plik, ensure_ascii=False, indent=4)

def comic_link(url):
    response = requests.get(url)
    return json.loads(response.text)['img']

def main():
    get_current_comic()
    pic_url = json_data["img"]
    pobierz(pic_url, "komiks.png")

    last_comic_num = json_data['num']

    if not os.path.exists(folder):
        os.mkdir(folder)

    for x in range(1, 11):
        pic_link = comic_link(pattern.format(num=last_comic_num - x))
        pic_name = os.path.basename(pic_link)
        pic_path = os.path.join(folder, pic_name)

        pobierz(pic_link, pic_path)
        print("Zapisałem komiks nr:", x)
        print("Sćieżka zapisu:", pic_path)


if __name__ == '__main__':
    main()
