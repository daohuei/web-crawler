import ast
import csv
import os
import re
from email.utils import parseaddr
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.command import Command

filename = 'email_output_from_bing_miami_0513_03.csv' #輸出後檔案（記得更改版本號 以免覆蓋前一個檔案
if os.path.isfile('./'+ filename):
	csvfile = open(filename, 'a', newline='')
	writer = csv.writer(csvfile)
else:
	csvfile = open(filename, 'a', newline='')
	writer = csv.writer(csvfile)
	# 寫入一列資料
	writer.writerow(['Business', 'Official Website', 'Facebook Page', 'Address', 'Email'])

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
options.add_experimental_option("prefs", prefs)
#options.add_argument('--headless') #背景運行
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')
# 開啟 CSV 檔案
bingoutputcsvfile = open('bing_result_Miami_0513_04.csv', newline='')  #輸入檔案（欲爬email的bing_result檔案
# 讀取 CSV 檔案內容
rows = csv.reader(bingoutputcsvfile)
rowscount = 0
for row in rows:
	if rowscount != 0:
		foundwebsite = row[1]
		emailstr = ''
		websitestr = ''
		if row[1] != 'none':
			websitestr = row[1]
			print(websitestr)
			browser.get(websitestr)
			websoup = BeautifulSoup(browser.page_source, "html.parser")
			websouplist = re.split(r'[><]', str(websoup))
			checkcontactlist = websoup.select('a')
			for websoupliststr in websouplist:
				if "@" in websoupliststr and "." in websoupliststr and '"' not in websoupliststr and ',' not in websoupliststr:
					for parsemailstr in parseaddr(websoupliststr):
						if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
							emailstr = parsemailstr
			if emailstr == "":
				for checkcontact in checkcontactlist:
					if len(re.findall("contact", checkcontact.get_text(), re.I)) > 0:
						if "http" in checkcontact['href'] or "www" in checkcontact['href']:
							browser.get(checkcontact['href'])
							websoup = BeautifulSoup(browser.page_source, "html.parser")
							websouplist = re.split(r'[><]', str(websoup))
							for websoupliststr in websouplist:
								if "@" in websoupliststr and "." in websoupliststr:
									if '"' not in websoupliststr and ',' not in websoupliststr:
										for parsemailstr in parseaddr(websoupliststr):
											if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
												emailstr = parsemailstr
						else:
							browser.get(re.sub(r'/\?fbclid=.*', '', browser.current_url) + "/" + checkcontact['href'])
							websoup = BeautifulSoup(browser.page_source, "html.parser")
							websouplist = re.split(r'[><]', str(websoup))
							for websoupliststr in websouplist:
								if "@" in websoupliststr and "." in websoupliststr:
									if '"' not in websoupliststr and ',' not in websoupliststr:
										for parsemailstr in parseaddr(websoupliststr):
											if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
												emailstr = parsemailstr
						break
		elif row[2] != 'none':
			websitestr = row[2] + 'about'
			print(websitestr)
			browser.get(websitestr)
			soup = BeautifulSoup(browser.page_source, "html.parser")
			eles = soup.select("._50f4")
			for ele in eles:
				websitestr = ""
				if "@" in ele.get_text():
					emailstr = ele.get_text()
				if "http" in ele.get_text():
					websitestr = ele.get_text()
					foundwebsite = ele.get_text()
			if websitestr != "":
				browser.get(websitestr)
				websoup = BeautifulSoup(browser.page_source, "html.parser")
				websouplist = re.split(r'[><]', str(websoup))
				checkcontactlist = websoup.select('a')
				for websoupliststr in websouplist:
					if "@" in websoupliststr and "." in websoupliststr and '"' not in websoupliststr and ',' not in websoupliststr:
						for parsemailstr in parseaddr(websoupliststr):
							if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
								emailstr = parsemailstr
				if emailstr == "":
					for checkcontact in checkcontactlist:
						if len(re.findall("contact", checkcontact.get_text(), re.I)) > 0:
							if "http" in checkcontact['href'] or "www" in checkcontact['href']:
								browser.get(checkcontact['href'])
								websoup = BeautifulSoup(browser.page_source, "html.parser")
								websouplist = re.split(r'[><]', str(websoup))
								for websoupliststr in websouplist:
									if "@" in websoupliststr and "." in websoupliststr:
										if '"' not in websoupliststr and ',' not in websoupliststr:
											for parsemailstr in parseaddr(websoupliststr):
												if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
													emailstr = parsemailstr
							else:
								browser.get(
									re.sub(r'/\?fbclid=.*', '', browser.current_url) + "/" + checkcontact['href'])
								websoup = BeautifulSoup(browser.page_source, "html.parser")
								websouplist = re.split(r'[><]', str(websoup))
								for websoupliststr in websouplist:
									if "@" in websoupliststr and "." in websoupliststr:
										if '"' not in websoupliststr and ',' not in websoupliststr:
											for parsemailstr in parseaddr(websoupliststr):
												if re.match(r"[^@]+@[^@]+\.[^@]+", parsemailstr):
													emailstr = parsemailstr
							break
		else:
			emailstr = 'none'
		if emailstr == '':
			emailstr = 'none'
		print(str(rowscount)+': '+emailstr)
		writer.writerow([row[0], foundwebsite, row[2], row[3], emailstr])
	rowscount += 1
csvfile.close()
browser.quit()
