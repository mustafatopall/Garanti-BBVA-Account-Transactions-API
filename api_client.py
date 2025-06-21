import requests
from config import API_URL

class APIClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.url = API_URL

    def get_transactions(self, payload):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(self.url, json=payload, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"API çağrısı başarısız. Status code: {response.status_code}")
                print(response.json())
                return None
        except Exception as e:
            print(f"İstek sırasında hata oluştu: {e}")
            return None
