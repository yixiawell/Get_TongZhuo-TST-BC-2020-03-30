import requests, os, re, concurrent.futures
from bs4 import BeautifulSoup
from urllib import parse
'''
detailurl = "http://www.tongzhuo100.com/v/2019-03/61194.html"
tsurl = "http://hla.tongzhuo100.com/hls/junior/eight/1C4CDGAC4N/2/1C4CDGAC4N-hls3.ts?auth_key=1584361955-0-0-5aae6bf8310114855697345c82d42e6c"
tsurl = "http://hla.tongzhuo100.com/hls/junior/eight/1CCDGGN44D/1/1C4CDGAC4N-hls2.ts?auth_key=1584361955-0-0-bb09e71491d95ec8f14e3c059f39c32a"
m3u8url = "http://hla.tongzhuo100.com/hls/junior/eight/1CCDGGN44D/2/1CCDGGN44D-hls.m3u8?auth_key=1584362814-0-0-312b47c7af8b16360c11e0c93d8f45f4"
http://www.tongzhuo100.com/primary/v1/8/38/index.html
http://hla.tongzhuo100.com/hls/junior/eight/1C4CDGAC4N/2/1C4CDGAC4N-hls.m3u8?auth_key=1584361955-0-0-1dc55b26e3856b43f7ed81e781596d0d
'''
class TongZhuo():
    def __init__(self):
        self.start_url = "http://www.tongzhuo100.com/primary/v1/7/3/index.html"
        self.title = None
        self.index_url = None
        self.reful_url = None

    def get_html(self, url):
        req = requests.get(url).content
        req = str(req, "utf-8")
        return req

    def get_detail_url(self):
        html = self.get_html(self.start_url)
        soup = BeautifulSoup(html,"lxml")
        detail_urls =[i["href"] for i in soup.select(".a1 a")]
        detail_title = [i["title"] for i in soup.select(".a1 a")]
        detail_list = list(zip(detail_title, detail_urls))
        for d in detail_list:
            self.get_m3u8_url(d[1], d[0])

    def get_m3u8_url(self, url, title):
        self.reful_url = url
        self.title = title
        print("正在下载：", title)
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")
        m3u8_url = soup.select("#parameter")[0]["titlexml"]
        compile_index_url = re.compile(r'(.*?/\d{1}/)')
        self.index_url = compile_index_url.findall(m3u8_url)[0]
        m3u8_txt = self.get_html(m3u8_url)
        if not os.path.exists(r".\视频"):
            os.mkdir(r".\视频")
        if not os.path.exists(r".\视频\{}".format(title)):
            os.mkdir(r".\视频\{}".format(title))
        path = r".\视频\{}\ts.m3u8".format(title)
        with open(r".\视频\{}\ts.m3u8".format(title), "w+") as f:
            f.write(m3u8_txt)
        self.get_ts(path)

    def get_ts(self, path):
        with open(path, "r") as f:
            a = f.readlines()
        ts_urls = [parse.urljoin(self.index_url, i.replace("\n","")) for i in a if i.find("#") == -1]
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as thread:
            fun_t = [thread.submit(self.get_ts_vido, t, path) for t in ts_urls]


    def get_ts_vido(self,ts_url, path):
        headers = {
            "Referer": "{}".format(self.reful_url),
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
        }
        file_name = ts_url[ts_url.rfind("-")+1:]
        html = requests.get(url=ts_url).content
        with open(os.path.join(path.replace("ts.m3u8",""), file_name.replace("\n","")),"wb+") as f:
            f.write(html)


if __name__ == '__main__':
    tongxue = TongZhuo()
    print("正在下载中。。。。")
    tongxue.get_detail_url()
    print("下载已完成")
