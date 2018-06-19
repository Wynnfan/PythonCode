import requests
from bs4 import BeautifulSoup
import os

path = 'E:/pycode/'

all_url = 'http://www.mzitu.com'

same_url = 'http://www.mzitu.com/page/'

header = {
    'User-Agent' : 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36 (KHTML,like Gecko Chrome/5.0.2662.102 UBrowser/6.1.2107.204 Safari/537.36'
}

start_html = requests.get(all_url,headers=header)

soup = BeautifulSoup(start_html.text,'html.parser')

page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text

for n in range(1,int(max_page) +1):
    ul = same_url+str(n)
    start_html = requests.get(ul,headers=header)
    soup = BeautifulSoup(start_html.text,'html.parser')
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text()
        if title!= '':
            print('准备爬取'+title)
            if os.path.exists(path+title.strip().replace('?','')):
                flag = 1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag = 0
            os.chdir(path+title.strip().replace('?',''))
            href = a['href']
            html = requests.get(href,headers=header)
            mess = BeautifulSoup(html.text,'html.parser')
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text
            if flag == 1 and len(os.listdir(path+title.strip().replace('?','')))>= int(pic_max):
                print('已保存，跳过')
            for num in range(1,int(pic_max)+1):
                pic = href+'/'+str(num)
                html = requests.get(pic,headers=header)
                mess = BeautifulSoup(html.text,'html.parser')
                pic_url = mess.find('img',alt = title)
                html = requests.get(pic_url['src'],headers=header)
                file_name = pic_url['src'].split(r'/')[-1]
                with open(file_name,'wb') as f:
                    f.write(html.content)
                    f.close()
            print('完成')
    print('第',n,'页完成')