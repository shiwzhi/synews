import requests
from lxml import etree
import os
import sys
import time
from bs4 import BeautifulSoup

current_dir = os.path.dirname(os.path.abspath(__file__))
dat_filename = current_dir+"/sy_news.dat"
dat_filename2 = dat_filename+"2"

def get_news():
	sy_url = "http://www.lpssy.edu.cn"

	r = requests.get(sy_url)

	r.encoding = 'utf-8'

	html = etree.HTML(r.text)

	href = html.xpath('//div[@id="TabTab03Con1"][1]//tr/td/table/tr')

	sy_news_list = []
	sy_news_txt = ""

	for i in href:
		single_news = "{} {} {}".format(i[1][0].text, i[0][0].attrib["title"], sy_url+i[0][0].attrib["href"])
		sy_news_list.append(single_news)

	for i in sy_news_list[:4]:
		sy_news_txt += i+'\n'

	return sy_news_txt

def get_news2():
	sy_url = "http://www.lpssy.edu.cn"
	r = requests.get(sy_url)

	r.encoding = 'utf-8'
	soup = BeautifulSoup(r.text, 'html.parser')
	temp1 = soup.find_all('tr')
	result = []
	result_list = []

	for i in temp1:
		if len(i.contents) == 2 and i.contents[0]['align'] == 'left' and i.contents[1]['align'] == 'right':
			result.append(i)
	result = result[:8]
	for i in result:
		result_list.append("{} {} {}".format(i.contents[1].contents[0].string,
			i.contents[0].contents[0]["title"].replace('\xa0',' '),
			sy_url+i.contents[0].contents[0]['href']))
	result_txt = ""
	for i in result_list[:4]:
		result_txt += i+"\n"
	return result_txt


#return true if pass time_interval
def is_time(time_interval):
	
	if not os.path.isfile(dat_filename):
		f = open(dat_filename, 'w')
		f.write(get_news())
		f.close()
	
	ftime = os.path.getmtime(dat_filename)
	return time.time() - ftime > time_interval

#return false if no new news and modify file time
#else return latest news and write to file
def check_news():
	if not os.path.isfile(dat_filename):
		f = open(dat_filename, 'w')
		news = get_news()
		f.write(news)
		f.close()
		# return news
	latest = get_news()
	current = open(dat_filename, 'r').read()
	if latest == current:
		os.utime(dat_filename,(time.time(), time.time()))
		return False
	else:
		f = open(dat_filename, 'w')
		f.write(get_news())
		f.close()
		return latest

def check_news2():
	if not os.path.isfile(dat_filename2):
		f = open(dat_filename2, 'w')
		news = get_news2()
		f.write(news)
		f.close()
		return news
	latest = get_news2()
	current = open(dat_filename2, 'r').read()
	if latest == current:
		os.utime(dat_filename2,(time.time(), time.time()))
		return False
	else:
		f = open(dat_filename2, 'w')
		f.write(get_news2())
		f.close()
		return latest
	
