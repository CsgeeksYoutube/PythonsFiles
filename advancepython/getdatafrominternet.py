import requests
result = requests.get("https://www.example.com/")
import bs4
a=bs4.BeautifulSoup(result.text,"lxml")
# print(a)
print(a.select('h1')[0].getText())
