import requests
import execjs



class OpenLawSpider():
    def __init__(self):
        self.url = "http://datamining.comratings.com/exam"
        self.headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 60.0) Gecko/20100101Firefox/60.0'
        }
        self.jscode = '''
session = "%s";
var encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

function f1(a) {
    var b, i, len;
    var c, c2, c3;
    len = a.length;
    i = 0;
    b = "";
    while (i < len) {
        c = a.charCodeAt(i++) & 0xff;
        if (i == len) {
            b += encoderchars.charAt(c >> 2);
            b += encoderchars.charAt((c & 0x3) << 4);
            b += "==";
            break
        }
        c2 = a.charCodeAt(i++);
        if (i == len) {
            b += encoderchars.charAt(c >> 2);
            b += encoderchars.charAt(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4));
            b += encoderchars.charAt((c2 & 0xf) << 2);
            b += "=";
            break
        }
        c3 = a.charCodeAt(i++);
        b += encoderchars.charAt(c >> 2);
        b += encoderchars.charAt(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4));
        b += encoderchars.charAt(((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6));
        b += encoderchars.charAt(c3 & 0x3f)
    }
    return b
}



function reload() {

        var a = "c1=" + f1(session.substr(1, 3)) + "; path=/";

        var b = "c2=" + f1(session) + "; path=/";
        return a+";"+b

}
reload();
    '''

    def get_val_v(self):
        js_res = requests.get(self.url, headers=self.headers)

        cookies = requests.utils.dict_from_cookiejar(js_res.cookies)
        return cookies

    def get_cookie(self):
        cookies = self.get_val_v()
        js = self.jscode % cookies['session']
        ctx = execjs.compile(js)
        cookie = ctx.call('reload')
        cookies = dict(cookies, **{i.split('=', 1)[0]: i.split('=', 1)[1] for i in cookie.split(';')})
        print(cookies)
        return cookies

    def get_page_html(self):
        cookies = self.get_cookie()
        page_res = requests.get(self.url, headers=self.headers, cookies=cookies)
        print(page_res.text[-6:])


if __name__ == "__main__":
    spider = OpenLawSpider()
    spider.get_page_html()