import requests
from io import BytesIO
def image_to_link(img, clientId):
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    url = "https://api.imgur.com/3/image"
    header = {
        "Authorization": f"Client ID {clientId}"
    }
    files = {
        "image": buffer
    }
    res = requests.post(url, headers=header, files=files)
    if res.status_code == 200:
        return res.json()['data']['link']
    else:
        print(res.text)
        return None