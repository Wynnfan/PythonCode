# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = ('utf-8')
        return r.text
    except:
        return '产生异常'

def get_content(html):
    url_list = []
    soup = BeautifulSoup(html,'lxml')
    cate_list = soup.find_all('div',class_='index_toplist mright mbottom')
    for cate in cate_list:
        name = cate.find('div',class_='toptab').find('span').get_text()
        with open('novel_list.csv','a+') as f:
            f.write("\n小说种类: {}\n".format(name))
            f.close()
        general_list = cate.find(style='display: block;')
        book_list = general_list.find_all('li')
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            url_list.append(link)
            with open('novel_list.csv','a') as f:
                f.write("小说名: {:} \n 小说地址: {:} \n".format(title,link))
if __name__ == '__main__':
    url = 'http://www.qu.la/paihangbang/'
    html = get_html(url)
    get_content(html)