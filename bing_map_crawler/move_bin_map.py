import math
import time
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import csv
import os
from selenium.webdriver.common.keys import Keys



long = 0.0
lat = 0.0
nwpos = list()  # 西北座標（須設定變數
nepos = list()  # 東北座標（須設定變數
swpos = list()  # 西南座標（須設定變數
sepos = list()  # 東南座標（須設定變數
placename = input('Input Position: ') #位置（須設定變數
if placename == 'NorthFlorida':
	# NorthFlorida
	nwpos = [30.99142, -87.59474]  # 西北座標（須設定變數
	nepos = [30.70768, -81.34805]  # 東北座標（須設定變數
	swpos = [29.58500, -87.64650]  # 西南座標（須設定變數
	sepos = [29.26934, -80.97023]  # 東南座標（須設定變數
elif placename == 'SouthFlorida':
	# SouthFlorida
	nwpos = [29.58500, -83.65614]  # 西北座標（須設定變數
	nepos = [28.85703, -78.94574]  # 東北座標（須設定變數
	swpos = [25.23647, -84.10035]  # 西南座標（須設定變數
	sepos = [24.67016, -79.63324]  # 東南座標（須設定變數
elif placename == 'Miami':
	# Miami
	nwpos = [25.840754, -80.322193]  # 西北座標（須設定變數
	nepos = [25.856263, -80.120034]  # 東北座標（須設定變數
	swpos = [25.703264, -80.317101]  # 西南座標（須設定變數
	sepos = [25.702224, -80.130558]  # 東南座標（須設定變數
elif placename == 'Brooklyn':
	# Brooklyn
	nwpos = [40.75509, -74.03146]  # 西北座標
	nepos = [40.71522, -73.80360]  # 東北座標
	swpos = [40.56014, -74.08593]  # 西南座標
	sepos = [40.51759, -73.85588]  # 東南座標
elif placename == 'Chicago':
	# Chicago
	nwpos = [42.03463, -87.96995]  # 西北座標
	nepos = [42.00929, -87.49084]  # 東北座標
	swpos = [41.66871, -87.98519]  # 西南座標
	sepos = [41.62945, -87.85120]  # 東南座標
elif placename == 'Houston':
	# Houston
	nwpos = [30.16000, -95.83510]  # 西北座標
	nepos = [30.16000, -95.03275]  # 東北座標
	swpos = [29.49471, -95.84467]  # 西南座標
	sepos = [29.46326, -95.01180]  # 東南座標
elif placename == 'LasVegas':
	# LasVegas
	nwpos = [36.39570, -115.42763]  # 西北座標
	nepos = [36.39356, -115.03769]  # 東北座標
	swpos = [36.12029, -115.42434]  # 西南座標
	sepos = [36.12132, -115.01976]  # 東南座標
elif placename == 'Houston2':
	# Houston2
	nwpos = [29.96302, -95.66447]  # 西北座標
	nepos = [29.96174, -95.11173]  # 東北座標
	swpos = [29.58976, -95.66391]  # 西南座標
	sepos = [29.57556, -95.07972]  # 東南座標
'''
'''

'''
'''

''''''

''''''
''''''
''''''
''''''
startpoint = list()
direction = 0
if swpos[0] <= sepos[0]:
	startpoint = swpos
else:
	startpoint = sepos
	direction = 1
west = abs(nwpos[0] - swpos[0])
east = abs(nepos[0] - sepos[0])
north = abs(nwpos[1] - nepos[1])
south = abs(sepos[1] - swpos[1])
if west >= east:
	long = west
else:
	long = east
if north >= south:
	lat = north
else:
	lat = south
querystr = quote_plus('transmission repair shop') #設定要搜尋的字串
lvl = int(input('lvl(14,13,12,11,10): '))#lvl是bingmap的放大比例尺
movelengthlist = [0.24*pow(0.5,lvl-10), 0.28*pow(0.5,lvl-10)]

longmovtimes = math.ceil(long/movelengthlist[1])
latmovtimes = math.ceil(long/movelengthlist[0])
filename = 'bing_result_'+placename+ '_lvl' + str(lvl) + '_time' + time.strftime("%m%d_%H%M%S", time.localtime()) +'.csv' #輸出檔名

if os.path.isfile('./'+ filename):
	csvfile = open(filename, 'a', newline='')
	writer = csv.writer(csvfile)
else:
	csvfile = open(filename, 'a', newline='')
	writer = csv.writer(csvfile)
	# 寫入一列資料
	writer.writerow(['Business', 'Official Website', 'Facebook Page', 'Address'])
checkrepeatlist = list()
url1 = 'https://www.bing.com/maps?cp='+ str(startpoint[0]) +'~'+ str(startpoint[1]) +'&lvl='+ str(lvl) +'&q='+ querystr + '&sst=1'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
#options.add_argument("--headless")
print('Opening Browser...')
browser = webdriver.Chrome(chrome_options=options,
                           executable_path='./chromedriver')
try:
	browser.get(url1)
	results = list()
	soup = BeautifulSoup(browser.page_source, "html.parser")
	totalcount = 0
	movecount = 0
	lvlcount = 0
	lvlcheckcount = 0
	while True:
		soup = BeautifulSoup(browser.page_source, "html.parser")
		time.sleep(0.5)
		more = browser.find_element(By.CSS_SELECTOR, '.taskBar .action a.moreIcon').click()
		time.sleep(0.5)
		likepage = browser.find_element(By.CSS_SELECTOR, 'a.dropdownEntry:nth-child(2)')
		likepage.click()
		time.sleep(0.5)
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		results = soup.select('.localListingListPrintText .printEntity')
		print(len(results))
		if len(results) != 0:
			closebutton = browser.find_element(By.CSS_SELECTOR, 'a.dialogClose.closeIcon')
			closebutton.click()
			time.sleep(0.5)
			for i in range(lvlcount):
				if lvlcheckcount == 0:#放大
					time.sleep(0.5)
					browser.find_element(By.CSS_SELECTOR, 'a#ZoomOutButton').click()
				else:#縮小
					time.sleep(0.5)
					browser.find_element(By.CSS_SELECTOR, 'a#ZoomInButton').click()
			
			time.sleep(0.5)
			more = browser.find_element(By.CSS_SELECTOR, '.taskBar .action a.moreIcon').click()
			time.sleep(0.5)
			likepage = browser.find_element(By.CSS_SELECTOR, 'a.dropdownEntry:nth-child(2)')
			likepage.click()
			time.sleep(0.5)
			soup = BeautifulSoup(browser.page_source, 'html.parser')
			results = soup.select('.localListingListPrintText .printEntity')
			
			break
		else:
			lvlcount += 1
			lvltotal = lvlcount + lvl
			
			if lvlcheckcount == 0:
				if lvltotal > 14:
					lvlcheckcount = 1
					lvlcount = 0
				else:
					browser.get(
						'https://www.bing.com/maps?cp=' + str(startpoint[0]) + '~' + str(startpoint[1]) + '&lvl=' + str(
							lvl + lvlcount) + '&q=' + querystr + '&sst=1')
					time.sleep(1)
			else:
				
				browser.get(
					'https://www.bing.com/maps?cp=' + str(startpoint[0]) + '~' + str(startpoint[1]) + '&lvl=' + str(
						lvl - lvlcount) + '&q=' + querystr + '&sst=1')
				time.sleep(1)
		
	for result in results:
		writename = ''
		writeadd = ''
		writeow = 'none'
		writefp = 'none'
		resultsoup = BeautifulSoup(str(result), 'html.parser')
		name = resultsoup.select('.localEntityPrintTitle')
		website = resultsoup.select('.localSearchPrintHeader.listingWebsite')
		address = resultsoup.select('.printEntityAddress .localSearchPrintHeader')
		writename = name[0].get_text()
		writeadd = address[0].get_text()
		if website[0].get_text() != "":
			if 'www.facebook.com' in website[0].get_text():
				writefp = website[0].get_text()
			else:
				writeow = website[0].get_text()
		checkrepeatflag = 0
		for checkrepeat in checkrepeatlist:
			if checkrepeat == writeadd:
				checkrepeatflag = 1
		if checkrepeatflag == 0:
			checkrepeatlist.append(writeadd)
			writer.writerow([writename, writeow, writefp, writeadd])
			totalcount += 1
			print(str(totalcount))
			print(name[0].get_text())
			print(website[0].get_text())
			
	closebutton = browser.find_element(By.CSS_SELECTOR, 'a.dialogClose.closeIcon')
	closebutton.click()
	time.sleep(0.5)
	print(str(round(float(movecount)*100 / float(longmovtimes * latmovtimes), 2)) + " %")
	for i in range(latmovtimes):
		for j in range(longmovtimes):
			if totalcount < 1000:
				if direction == 0:
					browser.find_element(By.CSS_SELECTOR, '.MicrosoftMap div.MicrosoftMap #mapFocus').send_keys(
						Keys.RIGHT)
					movecount+= 1
					time.sleep(1)
				else:
					browser.find_element(By.CSS_SELECTOR, '.MicrosoftMap div.MicrosoftMap #mapFocus').send_keys(
						Keys.LEFT)
					movecount+=1
					time.sleep(1)
				more = browser.find_element(By.CSS_SELECTOR, '.taskBar .action a.moreIcon').click()
				time.sleep(0.5)
				likepage = browser.find_element(By.CSS_SELECTOR, 'a.dropdownEntry:nth-child(2)')
				likepage.click()
				time.sleep(0.5)
				soup = BeautifulSoup(browser.page_source, 'html.parser')
				results = soup.select('.localListingListPrintText .printEntity')
				for result in results:
					writename = ''
					writeadd = ''
					writeow = 'none'
					writefp = 'none'
					resultsoup = BeautifulSoup(str(result), 'html.parser')
					name = resultsoup.select('.localEntityPrintTitle')
					website = resultsoup.select('.localSearchPrintHeader.listingWebsite')
					address = resultsoup.select('.printEntityAddress .localSearchPrintHeader')
					writename = name[0].get_text()
					writeadd = address[0].get_text()
					if website[0].get_text() != "":
						if 'www.facebook.com' in website[0].get_text():
							writefp = website[0].get_text()
						else:
							writeow = website[0].get_text()
					checkrepeatflag = 0
					for checkrepeat in checkrepeatlist:
						if checkrepeat == writeadd:
							checkrepeatflag = 1
					if checkrepeatflag == 0:
						checkrepeatlist.append(writeadd)
						writer.writerow([writename, writeow, writefp, writeadd])
						totalcount += 1
						print(str(totalcount))
						print(name[0].get_text())
						print(website[0].get_text())
				closebutton = browser.find_element(By.CSS_SELECTOR, 'a.dialogClose.closeIcon')
				closebutton.click()
				time.sleep(0.5)
				print(str(round(float(movecount)*100 / float(longmovtimes * latmovtimes), 2)) + " %")
		
		if totalcount < 1000:
			if direction == 0:
				direction = 1
			else:
				direction = 0
			browser.find_element(By.CSS_SELECTOR, '.MicrosoftMap div.MicrosoftMap #mapFocus').send_keys(Keys.UP)
			time.sleep(1)
			more = browser.find_element(By.CSS_SELECTOR, '.taskBar .action a.moreIcon').click()
			time.sleep(0.5)
			likepage = browser.find_element(By.CSS_SELECTOR, 'a.dropdownEntry:nth-child(2)')
			likepage.click()
			time.sleep(0.5)
			soup = BeautifulSoup(browser.page_source, 'html.parser')
			results = soup.select('.localListingListPrintText .printEntity')
			for result in results:
				writename = ''
				writeadd = ''
				writeow = 'none'
				writefp = 'none'
				resultsoup = BeautifulSoup(str(result), 'html.parser')
				name = resultsoup.select('.localEntityPrintTitle')
				website = resultsoup.select('.localSearchPrintHeader.listingWebsite')
				address = resultsoup.select('.printEntityAddress .localSearchPrintHeader')
				writename = name[0].get_text()
				writeadd = address[0].get_text()
				if website[0].get_text() != "":
					if 'www.facebook.com' in website[0].get_text():
						writefp = website[0].get_text()
					else:
						writeow = website[0].get_text()
				checkrepeatflag = 0
				for checkrepeat in checkrepeatlist:
					if checkrepeat == writeadd:
						checkrepeatflag = 1
				if checkrepeatflag == 0:
					checkrepeatlist.append(writeadd)
					writer.writerow([writename, writeow, writefp, writeadd])
					totalcount += 1
					print(str(totalcount))
					print(name[0].get_text())
					print(website[0].get_text())
			closebutton = browser.find_element(By.CSS_SELECTOR, 'a.dialogClose.closeIcon')
			closebutton.click()
			time.sleep(0.5)
			print(str(round(float(movecount)*100 / float(longmovtimes * latmovtimes), 2)) + " %")
	if totalcount < 1000:
		for j in range(longmovtimes):
			if direction == 0:
				browser.find_element(By.CSS_SELECTOR, '.MicrosoftMap div.MicrosoftMap #mapFocus').send_keys(Keys.RIGHT)
				time.sleep(1)
			else:
				browser.find_element(By.CSS_SELECTOR, '.MicrosoftMap div.MicrosoftMap #mapFocus').send_keys(Keys.LEFT)
				time.sleep(1)
			more = browser.find_element(By.CSS_SELECTOR, '.taskBar .action a.moreIcon').click()
			time.sleep(0.5)
			likepage = browser.find_element(By.CSS_SELECTOR, 'a.dropdownEntry:nth-child(2)')
			likepage.click()
			time.sleep(0.5)
			soup = BeautifulSoup(browser.page_source, 'html.parser')
			results = soup.select('.localListingListPrintText .printEntity')
			for result in results:
				writename = ''
				writeadd = ''
				writeow = 'none'
				writefp = 'none'
				resultsoup = BeautifulSoup(str(result), 'html.parser')
				name = resultsoup.select('.localEntityPrintTitle')
				website = resultsoup.select('.localSearchPrintHeader.listingWebsite')
				address = resultsoup.select('.printEntityAddress .localSearchPrintHeader')
				writename = name[0].get_text()
				writeadd = address[0].get_text()
				if website[0].get_text() != "":
					if 'www.facebook.com' in website[0].get_text():
						writefp = website[0].get_text()
					else:
						writeow = website[0].get_text()
				checkrepeatflag = 0
				for checkrepeat in checkrepeatlist:
					if checkrepeat == writeadd:
						checkrepeatflag = 1
				if checkrepeatflag == 0:
					checkrepeatlist.append(writeadd)
					writer.writerow([writename, writeow, writefp, writeadd])
					totalcount += 1
					print(str(totalcount))
					print(name[0].get_text())
					print(website[0].get_text())
			closebutton = browser.find_element(By.CSS_SELECTOR, 'a.dialogClose.closeIcon')
			closebutton.click()
			time.sleep(0.5)
			print(str(round(float(movecount)*100 / float(longmovtimes * latmovtimes), 2)) + " %")
	
	browser.quit()
except:
	print('Error')
	browser.quit()


csvfile.close()
