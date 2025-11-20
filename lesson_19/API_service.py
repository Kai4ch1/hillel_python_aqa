import requests
import random
import json
url = "https://images-api.nasa.gov/search?q=mars&media_type=image"

def random_photo(a, b) -> int:
    return random.randint(a, b)

def api_call():
    response = requests.get(url)
    response_json = response.json()
    data = response_json["collection"]["items"]

    return data

def save_random_photo(data, file_name : str):
    file_name += ".jpg"

    try:
        href = data[random_photo(0, 5)]["href"]
        nested_links = requests.get(url=href).json()
        photo = nested_links[random_photo(1, 4)]
        response = requests.get(url=photo)
        content = response.content
        with open(file_name, "wb") as ph:
                ph.write(bytes(content))
    except json.JSONDecodeError:
            print("Wrong photo format, upload the new ones and try again")


if __name__ == "__main__":
    nasa_files = api_call()
    save_random_photo(nasa_files, "photo_1")
    save_random_photo(nasa_files, "photo_2")