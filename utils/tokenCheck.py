import requests

def tokenChecker(token: str, Logger):
    header = {"Authorization": f"Bot {token}"}

    res = requests.get("https://discord.com/api/v10/users/@me", headers=header)
    Logger.LOAD(f"Api Status code: {res.status_code}")
    if res.status_code == 200:
        Logger.LOAD("Valid Token!")
        return True
    else:
        return False