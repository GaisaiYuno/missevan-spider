import requests
import time,sys,os
from urllib import request
from urllib import parse

def Print(data):
    print("name:"+data['name'])
    print("artist:"+data['artist'])

def GetLrc(q):#歌词下载函数
    q = parse.quote(q)
    url = "https://api.i-meto.com/meting/api?server=netease&type=parse&id="+q
    print ("requesting "+url)
    headers={ 
        "authority": "api.i-meto.com",
        "method": "GET",
        "path": "/meting/api?server=netease&type=parse&id="+q,
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "utf-8",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "dnt": "1",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "referer": "https://api.i-meto.com/music.page",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    response =  requests.get(url, headers = headers)
    response.encoding=response.apparent_encoding
    data=response.json()
    if (len(data)==0):
        return "No lrc!!!"
    for i in range(0,min(len(data)-1,10)):
        print("Num:"+(str)(i))
        Print(data[i])
        print("")
    print("num?")
    return data[(int)(input())]['lrc']

ans=""
while (True):
    q=(str)(input())
    if (q=="e"):
        break
    ret="lrc: \'"+GetLrc(q)+"\',\n"
    ans=ans+ret
    print(ret)

fout = open('lrc.js', 'w',encoding='utf8')
fout.write(ans)
fout.close()

