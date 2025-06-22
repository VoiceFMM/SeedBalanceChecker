import requests
from api import API_KEYS



NETWORKS = {
    "Ethereum": {
        "url": "https://api.etherscan.io/api",
        "token_id": "ethereum"
    },
    "BSC": {
        "url": "https://api.bscscan.com/api",
        "token_id": "binance"
    },
    "Polygon": {
    "url": "https://api.polygonscan.com/api",
    "token_id": "polygon"  
    },
}


def get_balance(url, address, api_key):
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        if data["status"] == "1":
            return int(data["result"]) / 10**18
        else:
            return None
    except Exception as e:
        print(f"❌ Помилка : {e}")
        return None

def ChecBalance(AdrList: list):
    
    address = AdrList
    for i in address:
        
            
        for name, net in NETWORKS.items():
            api_key = API_KEYS.get(name.lower())
            url = net["url"]
            token_id = net["token_id"]

            print(f"\n🌐 Мережа: {name}")

            if not api_key:
                print("⚠️ Відсутній API-ключ.")
                continue

            balance = get_balance(url, i[0], api_key)

            if balance is not None:
                print(f"Адреса {i[0]}")
                print(f"Seed - {i[3]}")
                print(f"💰 Баланс: {balance:.6f} {token_id.upper()}")
                if balance > 0:
                    return True
            else:
                print("❌ Невдалось отримати дані.")

    return False
            



