from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import ast

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')
url = "https://www.facebook.com/"
cookiefile = open('cookie.txt','r')
#cookiestr = cookiefile.read
cookienames=list()
cookievalues=list()
while True :
	cookietext = cookiefile.readline()
	if '"name"' in cookietext:
		cookiename = cookietext.split(",", 1)[0].split(" ")
		c = ''
		for cook in cookiename:
			if cook != '':
				c += cook
		cookienames.append(c)
	if '"value"' in cookietext:
		cookievalue = cookietext.split(",", 1)[0].split(" ")
		c = ''
		for cook in cookievalue:
			if cook != '':
				c += cook
		cookievalues.append(c)
	#l[n] = i,split("\t",1)
	if cookietext == '': break
browser.get(url)
cookiecount = 0
browser.delete_all_cookies()
for cookien in cookienames:
	browser.add_cookie(cookie_dict=ast.literal_eval('{'+cookien+','+cookievalues[cookiecount]+'}'))
	print(ast.literal_eval('{'+cookien+','+cookievalues[cookiecount]+'}'))
	cookiecount += 1

urlstr = 'https://www.facebook.com/profile.php?id=100005212455053&fref=pb&eid=ARBFL3wfE66Sj3mN0VRHKjPH9A7SHNTqOfnb_izyZlfvaj_9t1IYnljrwLKVXg8D0lB3MEt818wFmFo5&hc_location=profile_browser'
if 'id=' in urlstr:
	url = urlstr.split('&')[0] + '&sk=about'
else:
	url = urlstr.split('?')[0] + '/about'
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")
postselements = soup.select('#pagelet_timeline_medley_about div')
for postselement in postselements:
	try:
		if postselement['data-overviewsection'] == 'education':
			edusoup = BeautifulSoup(str(postselement), "html.parser")
			edus = edusoup.select('a')
			for edu in edus:
				if edu.get_text() != '':
					print('Education: '+edu.get_text())
	except KeyError:
		pass
	try:
		if postselement['data-overviewsection'] == 'places':
			plasoup = BeautifulSoup(str(postselement), "html.parser")
			plas = plasoup.select('a')
			for pla in plas:
				if pla.get_text() != '':
					print('Places: '+pla.get_text())
	except KeyError:
		pass



