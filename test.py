#  _*_ coding:gbk _*_

import xlrd 
import os
import sys

def statisticsForData():
	s = "你好"
	print(s)
	sheet = xlrd.open_workbook("subset.xls").sheet_by_index(0)
	print(os.path.abspath(os.path.dirname(sys.argv[0])))
	path = "C:\\Users\YANG\Desktop\KPI资料\Data\数据\\"
	fileNames= ["2014 count down Park 15min(12312014 235611)_20141231_235859",
				"2014 count down other areas 15mins(12312014 235624)_20141231_235923",
				"2014 count down Bay 15min(12312014 235550)_20141231_235909"]
	colIndexes = [9,17,25,26,27]
	thresholds = [[1,99.5,99.5,0.5,99.5],[2,100,100,0.000001,100]]
	for fileName in fileNames:
		sheet = xlrd.open_workbook(path+fileName+".xls").sheet_by_index(0) 
		for i in range(5):
			colIndex = colIndexes[i]
			x = sheet.col_values(colIndex)
			count1 = 0
			count2 = 0
			for j in range(8,len(x)):
				try:
					if(float(x[j])<thresholds[0][i]):
						count1 += 1 
					if(float(x[j])<thresholds[1][i]):
						count2 += 1 

				except:
					pass
			print(count1,count1/(len(x)-8),count2,count2/(len(x)-8))
		print(len(x)-8, "\n\n\n")


def REHtml():
	file = open("c:\\Users\yang\Desktop\PM.html")
	file.read()
	file.close()
	print(line)




if __name__=="__main__":
	REHtml()



