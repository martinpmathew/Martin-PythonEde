import requests

reply = requests.get("http://localhost:3000")
print(reply.status_code)
print(reply.headers['Content-Type'])
print(reply.text)
# print(requests.codes.__dict__)
