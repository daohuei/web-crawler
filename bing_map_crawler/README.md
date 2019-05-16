Bing Map Crawler
==================

<h2>參數Parameters</h2>
<h3>move_bin_map.py</h3>
<h4>placename</h4>

		placename = input('Input Position: ') #位置（於執行程式時輸入,只能輸入if/else條件式出現的placename

<h4>coordinate</h4>

		if placename == 'NorthFlorida':
		# NorthFlorida
		nwpos = [30.99142, -87.59474]  # 西北座標（須設定變數
		nepos = [30.70768, -81.34805]  # 東北座標（須設定變數
		swpos = [29.58500, -87.64650]  # 西南座標（須設定變數
		sepos = [29.26934, -80.97023]  # 東南座標（須設定變數

If you want to increase a option of a place to search, then add: 

		elif placename == 'place_you_want_to_search':
		# place_you_want_to_search
		nwpos = [latitude,longitude]   # 西北座標
		nepos = [latitude,longitude]   # 東北座標
		swpos = [latitude,longitude]   # 西南座標
		sepos = [latitude,longitude]   # 東南座標

<h4>Keyword</h4>

		querystr = quote_plus('transmission repair shop') #設定要搜尋的字串

<h4>比例尺scale</h4>

		lvl = int(input('lvl(14,13,12,11,10): '))#lvl是bingmap的放大比例尺, 輸入

lvl = 14 ->  2500 feet & 500 m

lvl = 13 ->  5000 feet & 1 km

lvl = 12 ->  1 miles & 2 km

lvl = 11 ->  2 miles & 5 km

lvl = 10 ->  5 miles & 10 km


<h3>csv_merge.py</h3>
<h4>bingoutputcsvfile1 & bingoutputcsvfile2</h4>
		
		bingoutputcsvfile1 = open('filename_output_from_move_bin_map_1', newline='') #擋案1,檔名必須先改成要結合的檔案
		bingoutputcsvfile2 = open('filename_output_from_move_bin_map_2', newline='') #檔案2,檔名必須先改成要結合的檔案

一次只能合成兩個csv檔

Input 一定要是從move_bin_map生成的csv


<h3>get_all_email.py</h3>
<h4>bingoutputcsvfile</h4>

		bingoutputcsvfile = open('csv檔案file', newline='')  #輸入檔案（欲爬email的bing_result檔案

此檔案必須為csv_merge.py或move_bin_map.py output的csv

<h4>輸出檔案(E-mail included)</h4>

		filename = '欲輸出的csv檔案filename' #輸出後檔案（記得更改版本號 以免覆蓋前一個檔案

***

<h2>Instructions</h2>

<h3>Steps</h3>

1. add the coordinate in move_bin_map.py by editting its code

2. python move_bin_map.py

3. Input Position: (placename)

4. lvl: (lvl)

5. (python csv_merge.py)(have to change the input filename in csv_merge.py first)

6. python get_all_email (have to change the input & output filename in get_all_email.py first)

<h3>注意</h3>

執行move_bin_map時盡量不要動到正在跑的browser

建議可同時執行多個move_bin_map比較有效率
