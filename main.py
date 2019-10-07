#encode: utf-8
import requests
import time,sys,os
import configparser
from urllib import request
from urllib import parse

ans=""
usetitle=0

#path_1='D:\HexoBlog\maintain\missevan-spider\mp3'
#path_2='D:\HexoBlog\maintain\missevan-spider\cover'

def init():

    global path
    path=os.getcwd()
    os.chdir(path)
    print(path)
    cf = configparser.ConfigParser()
    filename=cf.read("config.ini")
    #print (filename)
    global server,outfile,flag,usetitle,maxlrc
    #path=cf.get("music","path")
    server=cf.get("music","server")
    outfile=cf.get("music","outfile")
    flag=cf.getint("music","download")
    usetitle=cf.getint("music","usetitle")
    maxlrc=cf.getint("music","maxlrc")
    #print(maxlrc)

def cbk(a, b, c):#下载回调函数
    result=''
    global size
    size=c
    per = 100.0 * a * b / c
    if (per>100):
        per=100
    result=result+('%.2f%% ' % per)
    finished=per/2
    for i in range(1,50):
        if i<=finished:
            result=result+'#'
        else:
            result=result+'_'
    sys.stdout.write(result+"\r")
    sys.stdout.flush()

def download(path,url):#下载url的文件到path
    print("Downloading "+url+" to "+path)
    try:
        request.urlretrieve(url, path, cbk)
        print (60*'-')
        print ('Finish Downloading')
        size2=(float)(size/1024.000/1024.000)
        print ("Size=%.3fMB\n"%size2)
    except:
        print ("%s is a wrong url\n"%url)

def ext(path):
    return os.path.splitext(path)[1]

def Print(data):
    print("name:"+data['name'])
    print("artist:"+data['artist'])

def GetLrc(q):#歌词搜索函数
    q = parse.quote(q)
    url = "https://api.i-meto.com/meting/api?server="+server+"&type=parse&id="+q
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
    #print(len(data))
    #print(maxlrc)
    for i in range(0,min(len(data)-1,maxlrc)):
        print("Num:"+(str)(i))
        Print(data[i])
        print("")
    print("num?")
    num=(int)(input())
    global artist
    artist=data[num]['artist']
    return data[num]['lrc']

if __name__=="__main__":
    init()
    #print(maxlrc)
    while (True):
        print("Enter id,please:(Input e to end)")
        id=(input())
        if (id=="e"):
            break
        url = "https://www.missevan.com/sound/getsound?soundid="+id
        headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        response = requests.post(url, headers = headers)
        data=response.json()
        image_url=data['info']['sound']['front_cover']
        mp3_url="https://static.missevan.com/MP3/"+data['info']['sound']['soundurl']
        name=data['info']['sound']['soundstr']
        if (flag):
            download(path+'\\mp3\\'+name+ext(mp3_url),mp3_url)
            download(path+'\\cover\\'+name+ext(image_url),image_url)
        if (usetitle):
            print ("Enter Title:")
            name=(str)(input())
        lrc_url=GetLrc(name)
        now="{\n"+"    name: \'"+name+"\',\n    lrc: \'"+lrc_url+"\',\n"+"    url: \'"+mp3_url+"\',\n    cover: \'"+image_url+"\',\n"+"    artist: \'"+artist+"\',\n},\n\n"
        ans=ans+now
        print(now)

    print(ans)
    fout = open(outfile,'w',encoding='utf8')
    fout.write(ans)
    fout.close()
    os.system("pause")