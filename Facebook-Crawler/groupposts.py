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
import re
import ast

def pw(str,file):
   "This prints a passed string into this function"
   print(str)
   file.write(str+ "\n")
   return

#將粉絲專頁內所有貼文網址匯出
#url = input("Please input the website of Facebook Pages:") + "posts"
tStart = time.time()  # 計時開始

'''
# 自動登入
url = "https://www.facebook.com/"
account = "your_account"  # input("Please input Facebook account:")
pwd = "your_password"  # input("Please input Facebook password:")
'''

url = "https://www.facebook.com/"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument('--headless') #背景運行
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')

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
# comment_js_h > div > div > div > div:nth-child(2) > div > div > div >
# div.UFICommentContent > div._26f8 > div > span > div > span:nth-child(2)
# > span > span > span > span
#options.add_argument('--headless') #背景運行
'''
# 在瀏覽器打上網址連入
browser.get("https://www.facebook.com/groups/323858497946272/")

#//*[@id="feed_subtitle_1203879359645069;2207602792606049;;9"]/span[1]/span/a

browser.find_element_by_tag_name('body').send_keys(Keys.END)
'''
try:
    ele = WebDriverWait(browser, 2).until(
        expected_conditions.visibility_of_element_located(
            (By.ID, 'expanding_cta_close_button'))
    )
    sumbit2 = browser.find_element_by_id('expanding_cta_close_button').click()
    sys.stdout.write('Done')
    print('\nclose tab')
except TimeoutException:
	sys.stdout.write('Done')
	print('No need to close tab')
'''

#while True:
	#try:
sys.stdout.flush()

browser.execute_script("document.getElementById('pagelet_bluebar').remove();")
browser.execute_script("document.getElementById('headerArea').remove();")


print("Srearching...")
eles = browser.find_elements(By.CSS_SELECTOR, '.userContentWrapper')
coms = browser.find_elements(By.CSS_SELECTOR, '.UFICommentBody')

while True:
	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	time.sleep(0.5)
	WebDriverWait(browser, 10).until_not(expected_conditions.presence_of_element_located(
		(By.CSS_SELECTOR, '.uiMorePager.async_saving')))
	sys.stdout.write("\r")
	sys.stdout.write("\033[K")
	sys.stdout.write("find "+str(len(eles))+" posts and "+ str(len(coms)) +' comments')
	sys.stdout.flush()
	time.sleep(0.1)
	coms = browser.find_elements(By.CSS_SELECTOR, '.UFICommentBody')
	eles1 = browser.find_elements(By.CSS_SELECTOR, '.userContentWrapper')
	if len(eles) == len(eles1):
		sys.stdout.write("\r")
		sys.stdout.write("\033[K")
		sys.stdout.write("find "+str(len(eles))+" posts and "+ str(len(coms)) +' comments...Loading...')
		sys.stdout.flush()
		time.sleep(2)
		eles1 = browser.find_elements(By.CSS_SELECTOR, '.userContentWrapper')
		if len(eles) == len(eles1):
			break
		else:
			eles = eles1
	else:
		eles = eles1

for ele6 in browser.find_elements(By.CSS_SELECTOR, '.UFIPagerLink'):
	time.sleep(0.5)
	WebDriverWait(browser, 5).until_not(expected_conditions.presence_of_element_located(
		(By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
	actions = ActionChains(browser)
	actions.move_to_element(ele6).perform()
	time.sleep(0.5)
	ele6.click()
	coms = browser.find_elements(By.CSS_SELECTOR, '.UFICommentBody')
	sys.stdout.write("\r")
	sys.stdout.write("\033[K")
	sys.stdout.write("find " + str(len(eles)) + " posts and " + str(len(coms)) + ' comments')
	sys.stdout.flush()
for ele7 in browser.find_elements(By.CSS_SELECTOR, '.UFICommentLink'):
	time.sleep(0.5)
	WebDriverWait(browser, 5).until_not(expected_conditions.presence_of_element_located(
		(By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
	actions = ActionChains(browser)
	actions.move_to_element(ele7).perform()
	time.sleep(0.5)
	ele7.click()
	coms = browser.find_elements(By.CSS_SELECTOR, '.UFICommentBody')
	sys.stdout.write("\r")
	sys.stdout.write("\033[K")
	sys.stdout.write("find " + str(len(eles)) + " posts and " + str(len(coms)) + ' comments')
	sys.stdout.flush()
for ele5 in browser.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
	time.sleep(0.5)
	WebDriverWait(browser, 5).until_not(expected_conditions.presence_of_element_located(
		(By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
	actions = ActionChains(browser)
	actions.move_to_element(ele5).perform()
	time.sleep(0.5)
	ele5.click()
	coms = browser.find_elements(By.CSS_SELECTOR, '.UFICommentBody')
	sys.stdout.write("\r")
	sys.stdout.write("\033[K")
	sys.stdout.write("find " + str(len(eles)) + " posts and " + str(len(coms)) + ' comments')
	sys.stdout.flush()

##feed_subtitle_2111585345535935\3a 9\3a 0 > span.z_c3pyo1brp > span > a:nth-child(1)
##feed_subtitle_937865219625203\3b 1706906612721056\3b \3b 9 > span.z_c3pyo1brp > span > a
##feed_subtitle_937865219625203\3b 943641155714276\3b 0\3b 9 > span.z_c3pyo1brp > span > a

    # else:
    #	print("break")
    #	break
	#except TimeoutException:
		#print("break")
		#break

    # Close Browser
soup = BeautifulSoup(browser.page_source, "html.parser")
browser.quit()

postselements = soup.select('.userContentWrapper')
#['href']
i = 0
print('\nCreating Output...')
f = open('groupposts.txt', 'w')

for postselement in postselements:
	postsoup = BeautifulSoup(str(postselement), "html.parser")
	postsids = postsoup.select(' > div > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(1) > div > div > div > div > div > div > div > '
                       'span > span > a:nth-of-type(1)')
	postimgs = postsoup.select('.uiScaledImageContainer')
	postcontents = postsoup.select('.userContent')
	postsharecontents = postsoup.select('div.userContent ~ div .text_exposed_root')
	postlinks = postsoup.select('._3ekx > a')
	postlinkscontents = postsoup.select('._3n1k a')
	postlikes = postsoup.select('span._4arz > span')
	postcommentnums = postsoup.select('._36_q  a')
	postcommentcontents = postsoup.select('.UFICommentContent')

	if len(postsids) != 0:
		if postsids[0]['href'] != '#':
			a = 0
			b = 0
			c = 0
			pw("\n----------------\n", f)
			pw('Post Number:', f)
			pw(str(i+1), f)
			pw('Post Likes Count:', f)
			if len(postlikes) !=0:
				plk = postlikes[0].get_text()
				if ',' in plk:
					plk = plk.replace(',', '')
				pw(plk, f)
				a = int(plk)
			else:
				pw(str(0), f)
				a=0
			pw('Post Comments Count:', f)
			if len(postcommentnums) != 0:
				if len(postcommentnums) == 2:
					ttt = re.findall('\d+', postcommentnums[0].get_text())
					pcn = ''
					for tttt in ttt:
						pcn += tttt
					pw(pcn, f)
					b = int(pcn)
				else:
					if 'comment' in str(postcommentnums[0]):
						ttt = re.findall('\d+', postcommentnums[0].get_text())
						pcn = ''
						for tttt in ttt:
							pcn += tttt
						pw(pcn, f)
						b = int(pcn)
					else:
						pw(str(0), f)
						b = 0
			else:
				pw(str(0), f)
				b = 0
			pw('Post Shares Count:', f)
			if len(postcommentnums) != 0:
				if len(postcommentnums) == 2:
					ttt = re.findall('\d+', postcommentnums[1].get_text())
					psc = ''
					for tttt in ttt:
						psc += tttt
					pw(psc, f)
					c = int(psc)
				else:
					if 'shares' in str(postcommentnums[0]):
						ttt = re.findall('\d+', postcommentnums[0].get_text())
						psc = ''
						for tttt in ttt:
							psc += tttt
						pw(psc, f)
						c = int(psc)
					else:
						pw(str(0), f)
						c = 0
			else:
				pw(str(0), f)
				c = 0
			pw('Popular Number:', f)
			pw(str(a+b+c), f)
			pw('Link of the Post:', f)
			pw("https://www.facebook.com" + postsids[0]['href'], f)
			if postcontents[0].get_text() != "":
				pw('Post Content:', f)
				pw(postcontents[0].get_text(), f)
			# f.write('貼文內容：' + postcontents[0].get_text()+ "\n")
			else:
				pw('Post Content:', f)
				pw('None', f)
			# f.write('貼文內容：無'+ "\n")
			if len(postimgs) != 0:
				try:
					pw('Post Picture:', f)
					for postimg in postimgs:
						pw(postimg.parent['data-ploi'], f)
				# f.write('貼文照片：' + postimgs[i]['data-ploi']+ "\n")
				except KeyError:
					if postimg.img['src'] != '':
						pw(postimg.img['src'], f)
					else:
						pw('None', f)
				# f.write('貼文照片：無'+ "\n")
				except AttributeError:
					if postimg.img['src'] != '':
						pw(postimg.img['src'], f)
					else:
						pw('None', f)
				# f.write('貼文照片：無'+ "\n")
				except TypeError:
					if postimg.img['src'] != '':
						pw(postimg.img['src'], f)
					else:
						pw('None', f)
			else:
				pw('Post Picture:', f)
				pw('None', f)
			# f.write('貼文照片：' + postsrcs[0]['src']+ "\n")
			pw('Share Link:', f)
			if len(postlinks) != 0:
				pw(postlinks[0]['href'], f)
				pw('Share Link Content:', f)
				if len(postlinkscontents) != 0:
					pw(postlinkscontents[0].get_text(), f)
				else:
					pw('None', f)
			else:
				pw('None', f)
				pw('Share Link Content:', f)
				pw('None', f)

			pw('Share Post Content:', f)
			if len(postsharecontents) != 0:
				for postsharecontent in postsharecontents:
					pw(postsharecontent.get_text(), f)
			else:
				pw('None', f)
			pw('Comments:',f)
			for postcommentcontent in postcommentcontents:
				postcommentcontentsoup = BeautifulSoup(str(postcommentcontent), "html.parser")
				postcommentnames = postcommentcontentsoup.select('.UFICommentActorName')
				postcommentcontentdetails = postcommentcontentsoup.select('.UFICommentBody')
				pw('Account:'+postcommentnames[0].get_text(),f)
				try:
					pw('Account Link:www.facebook.com' + postcommentnames[0]['href'],f)
				except KeyError:
					pass
				if len(postcommentcontentdetails) != 0:
					pw('Comment Content:'+postcommentcontentdetails[0].get_text() + "\n",f)
				else:
					pw("\n",f)
			pw('End of Post',f)
			i += 1



f.close()
print("Crawling Completed")
tEnd = time.time()  # 計時結束
# 列印結果
print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位
print("Total %d Posts" % i)

