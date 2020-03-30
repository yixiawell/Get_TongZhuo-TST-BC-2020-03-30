'''
http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls3.ts?auth_key=1581251531-0-0-39adb6af07a06ad18e410e053492da21
http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls4.ts?auth_key=1581251531-0-0-0f1b1c963e4d8b664f2430b69721f393
http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls5.ts?auth_key=1581251531-0-0-a34e5f6aa51b08e37ed8b197018a9f04
http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls6.ts?auth_key=1581251531-0-0-824a2646b59ff9b51484ccb62138f8be
'''
#
# import requests
# url = ["http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls3.ts?auth_key=1581251531-0-0-39adb6af07a06ad18e410e053492da21",
#        "http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls4.ts?auth_key=1581251531-0-0-0f1b1c963e4d8b664f2430b69721f393",
#        "http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls5.ts?auth_key=1581251531-0-0-a34e5f6aa51b08e37ed8b197018a9f04",
#        "http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls6.ts?auth_key=1581251531-0-0-824a2646b59ff9b51484ccb62138f8be"
#        ]
# a = open("1.mp4","wb+")
# for u in url:
#     req = requests.get(u)
#     ree = req.content
#     a.write(ree)
# a.close()
# print(req.text)

# from urllib import parse
# url = "http://hla.tongzhuo100.com/hls/junior/eight/1CCAC4KK1N/2/1CCAC4KK1N-hls3.ts?auth_key=1581251531-0-0-39adb6af07a06ad18e410e053492da21"
# a = parse.unquote(url)
# print(a)

'''
"https://g-search1.alicdn.com/img/bao/uploaded/i4/i1/173275708/O1CN019HauGo1s2JKJJApBg-173275708.jpg_230x230.jpg_.webp"
"https://g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i3/121101819/O1CN01Pq1mqL1PJ91ohCIvF_!!0-saturn_solar.jpg_230x230.jpg_.webp"
'''
import re
url = "http://hla.tongzhuo100.com/hls/junior/eight/1C4CDGAC4N/2/1C4CDGAC4N-hls.m3u8?auth_key=1584361955-0-0-1dc55b26e3856b43f7ed81e781596d0d"
compile_index_url = re.compile(r'(.*?/\d{1}/)')
index_url = compile_index_url.findall(url)[0]
print(index_url)
