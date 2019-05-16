import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import sys

tStart = time.time()  # 計時開始

# 自動登入
url = "https://www.facebook.com/"
account = "youraccount"  # input("Please input Facebook account:")
pwd = "yourpassword"  # input("Please input Facebook password:")

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')
browser.get(url)
browser.find_element_by_id('email').send_keys(account)
browser.find_element_by_id('pass').send_keys(pwd)
browser.find_element_by_id('pass').send_keys(Keys.ENTER)

# keyword = input("Please input keywords:")
# browser.find_element_by_xpath("//input[@class='_1frb']").send_keys(keyword)
# browser.find_element_by_xpath("//input[@class='_1frb']").send_keys(Keys.ENTER)

# 從社團抓出所有成員
browser.get('group_member_page_website')
# browser.find_element_by_tag_name('body').send_keys(Keys.END)

js = "document.getElementById('pagelet_growth_expanding_cta').remove();"
js1 = "document.getElementById('headerArea').remove();"
js2 = "document.getElementById('u_0_g').remove();"
js3 = "document.querySelector('._1pfm').remove();"

try:
    browser.execute_script(js3)
    print(js3)
except WebDriverException:
    try:
        browser.execute_script(js)
        print(js)
    except WebDriverException:
        try:
            browser.execute_script(js1)
            print(js1)
        except WebDriverException:
            try:
                browser.execute_script(js2)
                print(js2)
            except WebDriverException:
                print('Still not work!?')

print("Srearching...")
eles = browser.find_elements(By.CSS_SELECTOR, '#groupsMemberSection_recently_joined .uiProfileBlockContent._61ce > div > div:nth-child(2) > div:nth-child(1) > a')
while True:
	browser.find_element_by_tag_name('body').send_keys(Keys.END)
	sys.stdout.write("\r")
	sys.stdout.write("\033[K")
	sys.stdout.write("find "+str(len(eles))+" members")
	sys.stdout.flush()
	time.sleep(1.5)
	eles1 = browser.find_elements(By.CSS_SELECTOR, '#groupsMemberSection_recently_joined .uiProfileBlockContent._61ce > div > div:nth-child(2) > div:nth-child(1) > a')
	if len(eles) == len(eles1):
		sys.stdout.write("\r")
		sys.stdout.write("\033[K")
		sys.stdout.write("find "+str(len(eles))+" members...Loading...")
		sys.stdout.flush()
		time.sleep(2)
		eles1 = browser.find_elements(By.CSS_SELECTOR, '#groupsMemberSection_recently_joined .uiProfileBlockContent._61ce > div > div:nth-child(2) > div:nth-child(1) > a')
		if len(eles) == len(eles1):
			break
		else:
			eles = eles1
	else:
		eles = eles1

soup = BeautifulSoup(browser.page_source, "html.parser")
adminmembernames = soup.select('#groupsMemberSection_admins_moderators .uiProfileBlockContent._61ce div._60ri > a')
membernames = soup.select('#groupsMemberSection_recently_joined .uiProfileBlockContent._61ce > div > div:nth-of-type(2) > div:nth-of-type(1) > a')


i = 0
for adminmembername in adminmembernames:
    print("Admin Member: "+adminmembername.get_text() + "\t" + adminmembername['href'])
    time.sleep(0.1)
    i += 1

j = 0
for membername in membernames:
    print("Member: "+membername.get_text() + "\t" + membername['href'])
    time.sleep(0.1)
    j += 1

print("Crawling Completed")
tEnd = time.time()  # 計時結束
# 列印結果
print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位
print("Total %d Admin Members" % i)
print("Total %d Members" % j)
