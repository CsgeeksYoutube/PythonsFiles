import requests
import bs4
# result = requests.get("https://www.example.com/") 

# a=bs4.BeautifulSoup(result.text,"lxml")
# # print(a)
# print(a.select('h1')[0].getText())


resq= requests.get('https://en.wikipedia.org/wiki/Swami_Vivekananda')
soup= bs4.BeautifulSoup(resq.text,'lxml')
# items= soup.select('.toctext')[0]
# # print(items.text)
# for item in soup.select('.toctext'):
#     print(item.text)
# print(soup.select('.thumbimage'))

imagelink=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Vivekananda_Image_August_1894.jpg/159px-Vivekananda_Image_August_1894.jpg')
# print(imagelink.content)
f=open('image.jpg','wb')
f.write(imagelink.content)
f.close()
