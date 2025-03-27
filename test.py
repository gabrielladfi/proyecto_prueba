import requests

API_URL = "http://64.23.177.194:3000/api/v1/prediction/fa2a3ad2-1808-45fb-8ec7-2fb88fb8df43"
headers = {"Authorization": "Bearer xm+VKiWhqVpfVBelJe/6TYJeGy6gxhAVadi3SyNXQ2M="}


def query(payload_message):
    payload = {
    "question": payload_message
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.text)


output = query("Qué servicios ofreces?")
    

