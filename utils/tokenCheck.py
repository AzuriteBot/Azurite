import requests

def tokenChecker(token):
    header = {"Authorization": token}
    res = requests.get(url='https://discord.com/api/v10/users/@me', headers=header)
    if res.status_code == 200:
        return True
    else:
        return False