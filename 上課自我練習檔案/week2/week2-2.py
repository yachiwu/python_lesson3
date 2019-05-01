#長條圖
import csv,datetime
def findSubCnt(filePath):
	fh = open(filePath,'r')
	csvFile = csv.DictReader(fh)

	subCntDict = dict()
	for row in csvFile:
		sid = int(row['StudentID'])
		if sid in subCntDict:
			subCntDict[sid]+=1
		else:
			subCntDict[sid] = 1
	fh.close()
	return subCntDict
import matplotlib.pyplot as py
subCnt = findSubCnt('midterm2.csv')
# seq = range(0,len(subCnt))
width = 0.35
# 只畫前三個
data=sorted(subCnt.items(), key=lambda d:d[1], reverse = True) #按照value排序
stid = []
frequency = []
for i in range(10): #取繳交最多次數的前10名
		stid.append(data[i][0])
		frequency.append(data[i][1])
# print(stid)		
# print(frequency)
py.bar(stid,frequency,width)
py.xticks(stid)

# py.bar(subCnt.keys(),subCnt.values(),width)
py.show()		

