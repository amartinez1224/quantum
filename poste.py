import requests

url = 'http://127.0.0.1:5000/postes'
myobj = {'x': 23,'y': 34,'dis': 4.67}

x = requests.post(url, data = myobj)

print(x.text)
