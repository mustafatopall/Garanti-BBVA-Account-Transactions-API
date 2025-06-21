class JSONParser:
    @staticmethod
    def parse_transactions(json_data):
        """
        API'den dönen JSON verisini alır, işlem listesini çıkarır.
        JSON yapısına göre burayı düzenle.
        """
        if not json_data:
            return []

        # Burada örnek olarak "result" altında "transactions" var diyelim:
        transactions = json_data.get("result", {}).get("transactions", [])
        # Eğer farklı yapıda ise buna göre düzenle

        # Örnek olarak işlemden önemli alanlar:
        parsed = []
        for t in transactions:
            parsed.append({
                "customerName": t.get("customerName", ""),
                "transactionId": t.get("transactionId", ""),
                "transactionDate": t.get("transactionDate", ""),
                "amount": t.get("amount", ""),
                "description": t.get("description", ""),
            })
        return parsed
