import os
import requests
from bs4 import BeautifulSoup

url='http://tieba.baidu.com/p/2166231880'
html =requests.get(url)
soup =BeautifulSoup(html.text,'html.parser')
img_urls=soup.findAll('img',bdwater='杉本有美吧,1280,860')
for img_url in img_urls:
    img_src=img_url['src']
    with open(os.path.split(img_src)[1],'wb') as f:
        f.write(requests.get(img_src).content)