import definitions
import requests

file_name = definitions.PATH_TO_NASA_PHOTO_1.name

URL = "http://127.0.0.1:8080/"

def post_file(filename=definitions.PATH_TO_NASA_PHOTO_1)-> dict:
    with open(filename, "rb") as file:
        files = {"image": file}
        response = requests.post(url=f"{URL}/upload", files=files)

        return response.json()

def get_file(link_for_photo):
    headers = {
        "Content-type": "text"
    }
    response = requests.get(url=f"{link_for_photo}", headers=headers)

    return response.json()

def delete_file(url_to_del):
    params = {
        "Content-type": "text"
    }
    response = requests.delete(url=url_to_del, headers=params)
    if response.status_code == 200:
        return print(f"Deleted Successfully, \nJSON={response.json()}")
    else:
        return print(f"File was not found, or error occurred, \n observe the status code={response.status_code}")



if __name__ == "__main__":
    get_link_of_photo = post_file() # 1. POST the photo.

    link = [str(x) for x in get_link_of_photo.values()][0]
    link_for_photo_str = link.replace("uploads", "image") # prep link to make the get request

    get_file(link_for_photo_str) # 2. GET the photo.
    URL_TO_DELETE_PHOTO = link_for_photo_str.replace("image", "delete") # prep the link to del the photo

    delete_file(URL_TO_DELETE_PHOTO) # 3. DELETE the photo.
