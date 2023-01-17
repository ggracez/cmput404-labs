import requests

print(requests.__version__)

print(requests.get("http://www.google.com"))

print(requests.get("https://raw.githubusercontent.com/ggracez/lab1/master/lab1.py").text)