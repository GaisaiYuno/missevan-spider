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
	#cf = configparser.ConfigParser()
	#filename=cf.read("config.ini")
	#global server,outfile,flag,usetitle,maxlrc
	#server=cf.get("music","server")
	#outfile=cf.get("music","outfile")
	#flag=cf.getint("music","download")
	#usetitle=cf.getint("music","usetitle")
	#maxlrc=cf.getint("music","maxlrc")

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

if __name__=="__main__":
	init()
	url="http://localhost:4000/raw/music.js"
	headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
	response=requests.get(url,headers=headers)
	print(response)
	data=response.json()
	print(data)
	for music in data:
		name=music['name']
		mp3_url=music['url']
		image_url=music['cover']
		lrc_url=''
		if ('lrc' in music):
			lrc_url=music['lrc']
		download(path+'\\mp3\\'+name+ext(mp3_url),mp3_url)
		download(path+'\\cover\\'+name+ext(image_url),image_url)
		if (not lrc_url==''):
			download(path+'\\lrc\\'+name+ext(lrc_url),lrc_url)
