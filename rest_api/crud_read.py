import requests

try:
    reply = requests.get("http://localhost:3000/")
except requests.RequestException:
    print("communication error!")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print("server error!")