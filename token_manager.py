import requests
from config import CLIENT_ID,CLIENT_SECRET,REDIRECT_URL,TOKEN_URL,SCOPE

def get_access_token():
    headers = {
        "Content_type": "application/x-www-form-urlencoded"

    }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URL,
        "scope": SCOPE
    }

    response = requests.post(TOKEN_URL,headers = headers,data=data)

    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access_token")
        print("✅ Token alındı.")
        return access_token
    else:
        print("❌ Token alınamadı.")
        print(f"Status Code: {response.status_code}")
        print(response.json())
        return None




