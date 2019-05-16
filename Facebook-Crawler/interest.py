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

#將粉絲專頁內所有貼文網址匯出
#url = input("Please input the website of Facebook Pages:") + "posts"
tStart = time.time()  # 計時開始
interests = list()
# 自動登入
'''
url = "https://www.facebook.com/"
account = ""  # input("Please input Facebook account:")
pwd = ""  # input("Please input Facebook password:")
'''
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
'''
browser.get(url)
browser.find_element_by_id('email').send_keys(account)
browser.find_element_by_id('pass').send_keys(pwd)
browser.find_element_by_id('pass').send_keys(Keys.ENTER)
'''
# comment_js_h > div > div > div > div:nth-child(2) > div > div > div >
# div.UFICommentContent > div._26f8 > div > span > div > span:nth-child(2)
# > span > span > span > span
#options.add_argument('--headless') #背景運行

# 在瀏覽器打上網址連入
browser.get("https://www.facebook.com/profile.php?id=100011164414525&fref=pb&eid=ARCkjOwqZdHX4lNYqB2cE7oP2td_oHRNoy9aWNsHOLOnQuR-If1nAmoGh5cSQqn6PAII-7s8Cp265IMW&hc_location=profile_browser")
more = browser.find_element(By.CSS_SELECTOR, '#fbTimelineHeadline > div:nth-of-type(2) > ul > li:nth-of-type(5) > div > a').click()
time.sleep(0.5)
likepage = browser.find_element(By.CSS_SELECTOR, '.uiContextualLayerPositioner.uiLayer > div > div > div > ul > li:nth-child(9) > a ')
likepage.click()

sys.stdout.flush()
print("Srearching...")
eles = browser.find_elements(By.CSS_SELECTOR, '#pagelet_timeline_medley_likes > div:nth-of-type(2) > div > ul > li')
while True:
	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	sys.stdout.write("\r")
	sys.stdout.write("\033")
	sys.stdout.write("find "+str(len(eles))+" interests")
	sys.stdout.flush()
	time.sleep(1.5)
	eles1 = browser.find_elements(By.CSS_SELECTOR, '#pagelet_timeline_medley_likes > div:nth-of-type(2) > div > ul > li')
	if len(eles) == len(eles1):
		sys.stdout.write("\r")
		sys.stdout.write("\033")
		sys.stdout.write("find "+str(len(eles))+" interests...Loading...")
		sys.stdout.flush()
		time.sleep(3)
		eles1 = browser.find_elements(By.CSS_SELECTOR, '#pagelet_timeline_medley_likes > div:nth-of-type(2) > div > ul > li')
		if len(eles) == len(eles1):
			break
		else:
			eles = eles1
	else:
		eles = eles1

soup = BeautifulSoup(browser.page_source, "html.parser")
# browser.quit()
interestnames = soup.select('#pagelet_timeline_medley_likes > div:nth-of-type(2) > div > ul > li > div > div > div > div > div > div > a')
interesttypes = soup.select('#pagelet_timeline_medley_likes > div:nth-of-type(2) > div > ul > li > div > div > div > div > div > div:nth-of-type(2)')
#['href']
x = 0
i = 0
print('\nCreating Output...')
for interestname in interestnames:
	if interestname['href'] != '#':
		if len(interests) > 0:
			n = 1
			#print(interestname.get_text()+"\n"+interestname['href']+"\n"+interesttypes[i].get_text())
			for interest in interests:
				if interesttypes[i].get_text() == interest[0]:
					interest[1] += 1
					break
				else:
					if n == len(interests):
						arr=[interesttypes[i].get_text(),1]
						interests.append(arr)
						x += 1
						break
					else:
						n += 1
		else:
			arr = [interesttypes[i].get_text(), 1]
			interests.append(arr)
    #print("https://www.facebook.com" + postsid['href'])
    #time.sleep(0.1)
	i += 1

y = 0
for interest in interests:
	if y > 0:
		interest2 = interests[y]
		for u in range(y):
			interest1 = interests[y - u - 1]
			if interest2[1] > interest1[1]:
				interests[y - u - 1] = interest2
				interests[y - u] = interest1
			
			u += 1
	y += 1
print("Crawling Completed")
tEnd = time.time()  # 計時結束
# 列印結果
for outcome in interests:
	print(outcome[0]+"("+str(outcome[1])+")")
print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位
print("Total %d Interests" % i)
print("Total %d Types" % x)
