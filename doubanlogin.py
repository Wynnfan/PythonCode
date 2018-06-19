import requests

class DoubanClient():
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4)'
                          ' AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.116Safari / 537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(headers)
    def login(self, username, password,
              source = 'index_nav',
              ):
        url = 'http://www.douban.com/accounts/login'
        r = requests.get(url)
        data = {
                'form_email': username,
                'form_password': password,
                'source': source
        }
        headers = {
            'Referer': 'https://www.douban.com/',
            'Host': 'www.douban.com'
        }
        r = self.session.post(url, data=data, headers=headers)
        print(self.session.cookies.items())

if __name__ == '__main__':
    c = DoubanClient()
    c.login('15956940682', 'Wf19970611')