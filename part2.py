# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

print('請選擇看板:')
board=input('MobileComm,Hate,Food,TaiwanDrama,Gossiping,KoreaDrama,Transfer...')
url="https://www.ptt.cc/bbs/"+board+"/index.html"
page=input('抓取幾頁資料:')

def get_article_content(article_url): #文章內容解析
	r = requests.get(article_url)
	soup = BeautifulSoup(r.text, "lxml")
	results = soup.select('span.article-meta-value')
	content = soup.select('.bbs-screen.bbs-content')

	print('日期:', results[3].text)
	print('作者:', results[0].text)
	print('標題:', results[2].text)
	print('看板名稱:', results[1].text)
	print('內文:')
	print(content[0].text)



def get_all_href(url): #得到每一文章網址
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	results = soup.select("div.title")
	for item in results:
		a_item = item.select_one("a")
		title = item.text
		if a_item:
			get_article_content('https://www.ptt.cc'+ a_item.get('href'))

get_all_href(url) #第一頁
for page in range(page-1): #抓取頁數
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	btn = soup.select('div.btn-group > a')
	up_page_href = btn[3]['href']
	next_page_url = 'https://www.ptt.cc' + up_page_href #上一頁網址
	url = next_page_url
	get_all_href(url)