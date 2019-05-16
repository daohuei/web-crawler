import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import ast

def crawlfunc(bro, url, i):
	global pagecount
	f = open("fanpagematch.txt",'w')
	likebound = int(input("Input Like Bounds: "))
	kstr = input("Input Keyword: ")
	while True:
		pagelikechecklist = list()
		checkcount = 0
		bro.get(url + str(i))
		soup = BeautifulSoup(bro.page_source, "html.parser")
		pageselements = soup.select('._4-u2._6x0a._4-u8')
		for pageselement in pageselements:
			pagesoup = BeautifulSoup(str(pageselement), "html.parser")
			pagenames = pagesoup.select('._6x0d ')
			pagelikes = pagesoup.select('._4bl9')
			pagecontents = pagesoup.select('._ajw')
			if ',' in pagelikes[0].get_text().split(pagenames[0].get_text())[1].split(" ")[0]:
				likecount = float(pagelikes[0].get_text().split(pagenames[0].get_text())[1].split(" ")[0].replace(',', ''))
			elif 'K' in pagelikes[0].get_text().split(pagenames[0].get_text())[1].split(" ")[0]:
				likecount = float(pagelikes[0].get_text().split(pagenames[0].get_text())[1].split(" ")[0].split("K")[0])*1000.0
			else:
				likecount = float(pagelikes[0].get_text().split(pagenames[0].get_text())[1].split(" ")[0])
			pagelikechecklist.append(likecount)
			if likecount >= likebound:
				if len(re.findall(kstr, pagecontents[0].get_text(), re.I)) > 0:
					print(pagenames[0].get_text())
					print(pagenames[0]['href'])
					f.write(pagenames[0].get_text()+"*#$%*"+pagenames[0]['href']+"\n")
					print(likecount)
					print(pagecontents[0].get_text())
					pagecount += 1
		for pagelikecheck in pagelikechecklist:
			if pagelikecheck < likebound:
				checkcount += 1
			if checkcount == len(pagelikechecklist):
				return
		i += 1
	f.close()
	browser.quit()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
#options.add_argument('--headless') #背景運行
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')
url = "https://www.facebook.com/"
cookiefile = open('cookie.txt', 'r')
# cookiestr = cookiefile.read
cookielines = list()
while True:
	cookietext = cookiefile.readline()
	cookielines.append(cookietext.split("\n")[0])
	if cookietext == '': break
browser.get(url)
browser.delete_all_cookies()
cookielines.pop()
for cookieline in cookielines:
	browser.add_cookie(cookie_dict=ast.literal_eval(cookieline))
urllink = "https://www.facebook.com/pages/category/automotive-restoration/?page="
pagecount = 0
count = 1
crawlfunc(browser,urllink,count)
print("Total "+str(pagecount)+" pages match keywords")
