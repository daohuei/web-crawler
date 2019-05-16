import csv
import time

bingoutputcsvfile1 = open('bing_result_Florida_lvl10_time0514_192515.csv', newline='') #擋案1
# 讀取 CSV 檔案內容
rows1 = csv.reader(bingoutputcsvfile1)

bingoutputcsvfile2 = open('bing_result_Florida_lvl10_time0514_175658.csv', newline='') #檔案2
# 讀取 CSV 檔案內容
rows2 = csv.reader(bingoutputcsvfile2)
newlist = list()
for row1 in rows1:
	newlist.append(row1)
rowscount = 0
for row in rows2:
	repeatcheck = 0
	if rowscount != 0:
		for newrow in newlist:
			if row[3] == newrow[3]:
				repeatcheck = 1
		if repeatcheck == 0:
			newlist.append(row)
	rowscount += 1
			
filename = 'bing_result_merge_time' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +'.csv' #結合後檔案

csvfile = open(filename, 'a', newline='')
writer = csv.writer(csvfile)

for nwrow in newlist:
	writer.writerow(nwrow)

csvfile.close()
