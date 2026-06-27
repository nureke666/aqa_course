import os
import requests


def test_download_avatar():
    response = requests.get("https://dummyjson.com/icon/emilys/128")
    assert response.status_code == 200

    with open("emily_avatar.png", "wb") as file:
        file.write(response.content)

    assert os.path.exists("emily_avatar.png") == True, "File doesn't exist"
    assert os.path.getsize("emily_avatar.png") > 0, "File is empty"


def test_upload_avatar():
    URL = "https://postman-echo.com/post"

    with open("emily_avatar.png", "rb") as file:
        files_dict = {"avatar": file}
        response = requests.post(URL, files=files_dict)
        print(response.json())
        assert response.status_code == 200
        assert "emily_avatar.png" in response.json()["files"]
