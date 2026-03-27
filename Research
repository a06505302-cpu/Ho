import requests
import time

# رابط تحديث DuckDNS
url = "https://www.duckdns.org/update?domains=Gatecheck&token=58942b91-0ff6-466e-bad7-3940469677b8"

while True:
    try:
        response = requests.get(url, verify=False, timeout=10)  # تجاهل مشاكل الشهادة
        print("DuckDNS response:", response.text)  # لو OK يبقى اتحدث بنجاح
    except Exception as e:
        print("Error:", e)
    time.sleep(240)  # 240 ثانية = 4 دقائق
