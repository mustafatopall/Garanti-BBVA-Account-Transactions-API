from token_manager import get_access_token
from api_client import APIClient
from json_parser import JSONParser
from data_display import DataDisplay

def main():
    token = get_access_token()
    if not token:
        print("Token alınamadığı için program sonlandırılıyor.")
        return

    client = APIClient(token)
    payload = {
        "consentId": "3e09da8a-ae9c-50bc-b34a-c61531729dbe",
        "unitNum": 295,
        "accountNum": 6291296,
        "IBAN": "TR620006200029500006291296",
        "startDate": "2020-12-25T12:53:07.867",
        "endtDate": "2020-12-25T17:53:07.867",
        "transactionId": "",
        "pageIndex": 1,
        "pageSize": 20
    }

    json_data = client.get_transactions(payload)
    transactions = JSONParser.parse_transactions(json_data)

    display = DataDisplay(transactions)
    display.run()

if __name__ == "__main__":
    main()
