import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import ast
import os
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
import sys
from multiprocessing import Process

def usr_login():
	options = webdriver.ChromeOptions()
	options.add_argument("--incognito")
	options.add_argument("--start-maximized")
	print('Opening Browser...')
	browser = webdriver.Chrome(chrome_options=options,
	                           executable_path='./chromedriver')
	url = "https://www.facebook.com/"
	Account = entry_usr_name.get()
	Pwd = entry_usr_pwd.get()
	browser.get(url)
	browser.find_element_by_id('email').send_keys(Account)
	browser.find_element_by_id('pass').send_keys(Pwd)
	browser.find_element_by_id('pass').send_keys(Keys.ENTER)
	newcookiefile = open('cookie.txt', 'w')
	for newcookie in browser.get_cookies():
		newcookiefile.write(str(newcookie) + "\n")
	newcookiefile.close()
	browser.quit()
	win.destroy()
	initiatewindow2()
def usr_sign_up():
	for terminatep in proc:
		terminatep.terminate()
	for closebro in bro:
		closebro.quit()
	sys.exit('Goodbye')
def startautoapprove():
	global proc
	global bro
	options = webdriver.ChromeOptions()
	options.add_argument("--incognito")
	options.add_argument("--start-maximized")
	# options.add_argument("--headless")
	print('Opening Browser...')
	bro.append(webdriver.Chrome(chrome_options=options,
	                            executable_path='./chromedriver'))
	p = Process(target=autoapproveprocess)
	p.start()
	proc.append(p)
def initiatewindow2():
	global entry_group_name
	global entry_time
	window2 = tk.Tk()
	window2.title('Auto Approve System')
	window2.geometry('800x200')
	tk.Label(window2, text='Group Address: ').place(x=50, y=50)  # 创建一个`label`名为`User name: `置于坐标（50,150）
	tk.Label(window2, text='Time for loop: ').place(x=50, y=90)
	var_group_name = tk.StringVar()  # 定义变量
	var_group_name.set('https://www.facebook.com/groups/2444210305797761')  # 变量赋值'example@python.com'
	entry_group_name = tk.Entry(window2,
	                            textvariable=var_group_name,
	                            width=500)  # 创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
	entry_group_name.place(x=160, y=50)
	var_time = tk.StringVar()
	entry_time = tk.Entry(window2, textvariable=var_time)  # `show`这个参数将输入的密码变为`***`的形式
	entry_time.place(x=160, y=90)
	btn_startautoapprove = tk.Button(window2, text='Start',
	                                 command=startautoapprove)  # 定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
	btn_startautoapprove.place(x=130, y=130)
	btn_Leave = tk.Button(window2, text='Leave', command=usr_sign_up)
	btn_Leave.place(x=230, y=130)
	window2.mainloop()

def initiatewindow1(window):
	global entry_usr_name
	global entry_usr_pwd
	window.title('Auto Approve System')
	window.geometry('400x200')
	# user information
	tk.Label(window, text='Facebook Account: ').place(x=50, y=50)  # 创建一个`label`名为`User name: `置于坐标（50,150）
	tk.Label(window, text='Password: ').place(x=50, y=90)

	var_usr_name = tk.StringVar()  # 定义变量
	var_usr_name.set('example@facebook.com')  # 变量赋值'example@python.com'
	entry_usr_name = tk.Entry(window,
	                          textvariable=var_usr_name)  # 创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
	entry_usr_name.place(x=160, y=50)
	var_usr_pwd = tk.StringVar()
	entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')  # `show`这个参数将输入的密码变为`***`的形式
	entry_usr_pwd.place(x=160, y=90)

	# login and sign up button
	btn_login = tk.Button(window, text='Login', command=usr_login)  # 定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
	btn_login.place(x=170, y=130)
	btn_sign_up = tk.Button(window, text='Leave', command=usr_sign_up)
	btn_sign_up.place(x=270, y=130)
	window.mainloop()

def autoapproveprocess():

	url = "https://www.facebook.com/"
	cookiefile = open('cookie.txt', 'r')
	# cookiestr = cookiefile.read
	cookielines = list()
	while True:
		cookietext = cookiefile.readline()
		cookielines.append(cookietext.split("\n")[0])
		if cookietext == '': break
	bro[len(bro)-1].get(url)
	bro[len(bro)-1].delete_all_cookies()
	cookielines.pop()
	for cookieline in cookielines:
		bro[len(bro)-1].add_cookie(cookie_dict=ast.literal_eval(cookieline))
	t = int(entry_time.get())
	url = entry_group_name.get() + '/admin_activities/'
	while True:
		bro[len(bro)-1].get(url)
		soup = BeautifulSoup(bro[len(bro)-1].page_source, "html.parser")
		requests_count = soup.select('#count_badge_requests')
		if requests_count[0].get_text() != "0":
			eleapprove = bro[len(bro)-1].find_elements(By.CSS_SELECTOR,
			                                   '#groupsUnifiedQueueLHCTabs ul.uiList > li:nth-of-type(3) a')
			actions = ActionChains(bro[len(bro)-1])
			actions.move_to_element(eleapprove[0]).perform()
			time.sleep(0.5)
			eleapprove[0].click()
			try:
				ele = WebDriverWait(bro[len(bro)-1], 5).until(
					expected_conditions.visibility_of_element_located(
						(By.NAME, 'approve_all'))
				)
				allaprove = bro[len(bro)-1].find_element(By.NAME, 'approve_all')
				actions = ActionChains(bro[len(bro)-1])
				actions.move_to_element(allaprove).perform()
				time.sleep(0.5)
				allaprove.click()
				try:
					ele = WebDriverWait(bro[len(bro)-1], 5).until(
						expected_conditions.visibility_of_element_located(
							(By.CSS_SELECTOR, '.layerConfirm'))
					)
					layerConfirm = bro[len(bro)-1].find_element(By.CSS_SELECTOR, '.layerConfirm')
					actions = ActionChains(bro[len(bro)-1])
					actions.move_to_element(layerConfirm).perform()
					time.sleep(0.5)
					layerConfirm.click()
				except TimeoutException:
					print('No member need approve!')
			except TimeoutException:
				print('No member need approve!')
		else:
			print('No member need approve!')
		time.sleep(t)

win = tk.Tk()
win.quit()
entry_usr_name = tk.Entry()
entry_time = tk.Entry()
entry_group_name = tk.Entry()
entry_usr_pwd = tk.Entry()
proc = list()
bro = list()
if __name__ == '__main__':
	if os.path.isfile('./cookie.txt') == False:
		initiatewindow1(win)
	else:
		win.destroy()
		initiatewindow2()
