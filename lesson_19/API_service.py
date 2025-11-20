import requests
import random
import json
url = "https://images-api.nasa.gov/search?q=mars&media_type=image"

def random_photo(a, b) -> int:
    return random.randint(a, b)

def random_collection(a, b) -> int:
    return random.randint(a, b)

def api_call():
    response = requests.get(url)
    response_json = response.json()
    data = response_json["collection"]["items"]

    return data

def save_random_photo(data, file_name : str, count):
    count += 1
    file_name += f"{count}.jpg"

    with open(file_name, "wb") as ph:
        try:
            href = data[random_collection(0, 5)]["href"]
            nested_links = requests.get(url=href).json()
            photo = nested_links[random_photo(1, 4)]
            response = requests.get(url=photo)
            content = response.content
            ph.write(bytes(content))
        except json.JSONDecodeError:
            print("Wrong photo format, upload the new ones and try again")


if __name__ == "__main__":
    nasa_files = api_call()
    save_random_photo(nasa_files, "photo_", 0)
    save_random_photo(nasa_files, "photo_", 1)