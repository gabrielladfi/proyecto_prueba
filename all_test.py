import requests


API_URL1 = "http://64.23.177.194:3000/api/v1/prediction/2d4efde4-2262-4ab6-ac2e-16e866ac5576"
API_URL2 = "http://64.23.177.194:3000/api/v1/prediction/0ac635b0-b416-4725-b8d6-ab9d21e28743"
API_URL3 = "http://64.23.177.194:3000/api/v1/prediction/1d57a30c-869e-4e30-86d4-1a98f4580476"
API_URL4 = "http://64.23.177.194:3000/api/v1/prediction/e67e609d-18d9-435a-8eda-667b42e19f60"

ALL_URLS = []

ALL_URLS.append(API_URL1)
ALL_URLS.append(API_URL2)
ALL_URLS.append(API_URL3)
ALL_URLS.append(API_URL4)


headers = {"Authorization": "Bearer xm+VKiWhqVpfVBelJe/6TYJeGy6gxhAVadi3SyNXQ2M="}


def query(payload_message):
    payload = {
    "question": payload_message
    }
    for API_URL in ALL_URLS:
        print("========= New Request ==========")
        print(API_URL)
        response = requests.post(API_URL, headers=headers, json=payload)
        print(response.text)
        print("========= End Request ==========")


output = query("Qué servicios ofreces?")
    

