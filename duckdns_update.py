import requests
import time

url = "https://www.duckdns.org/update?domains=Gatecheck&token=58942b91-0ff6-466e-bad7-3940469677b8"

while True:
    try:
        response = requests.get(url, timeout=10)  # بدون verify=False عشان SSL مظبوط
        print("DuckDNS response:", response.text)
    except Exception as e:
        print("Error:", e)
    time.sleep(240)  # كل 4 دقائق
