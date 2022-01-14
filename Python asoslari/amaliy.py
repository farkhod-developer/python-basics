# from  a18_dars_modullar import Nomer
# with open(a18_dars_modullar, 'r') as asd:
#     a = asd.readlines()

# if '+998-90-588-99-78\n' in a:
#     print('Muhammadali')
# else:
#     print('yoq')


import requests
from bs4 import BeautifulSoup
sahifa = 'https://kun.uz/news/main'
r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_= 'news.title')
print(news[0].text)