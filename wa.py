# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def GetHtml(url):
    proxies = {'http': '58.249.55.222'}
    try:
        r = requests.get(url, proxies=proxies, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

def ParseHtml(html):

    #电影名
    movie_names = []
    soup = BeautifulSoup(html,'html.parser')
    name = soup.find_all('div',class_='hd')
    for each in name:
        try:
            movie_names.append(each.a.span.text)
        except:
            print('电影名爬取失败')
    #电影资料
    messages = []
    message = soup.find_all('div',class_='bd')
    for each in message:
        try:
            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
        except:
            continue
    #评分
    stars = []
    star = soup.find_all('span',class_='rating_num')
    for each in star:
        try:
            stars.append(' 评分：%s' % each.text)
        except:
            continue

    result = []
    for i in range(len(movie_names)):
        result.append(movie_names[i] + messages[i] + stars[i] + '\n')

    return result

def save_data(data):
    with open('movies.txt', 'w+',encoding='utf-8') as f:
        for each in data:
            f.write(each)
            f.close()


if __name__ == '__main__':
    host = 'https://movie.douban.com/top250'
    html = GetHtml(host)
    result = []
    for i in range(10):
        url = host + '/?start=' + str(25 * i)
        html = GetHtml(url)
        result.extend(ParseHtml(html))
    save_data(result)




