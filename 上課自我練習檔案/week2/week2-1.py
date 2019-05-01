#測試用
# import matplotlib.pyplot as py
# x = range(1,6)
# y = [4,2,5,1,6]
# py.plot(x,y)
# py.show()
#直方圖 histogram 說明越接近考試尾聲submission 次數越多
#直方圖特色: [0,1000)(不包含1000),[1000,2000)
import csv,datetime
def findSubTimes(filename):
	fh = open(filename,'r')
	csvfile = csv.DictReader(fh)

	subTime = [] #to store submission times
	for row in csvfile:
		dt = datetime.datetime.strptime(row["SubmissionTime"],"%H:%M:%S").time()#time()產生time object
		sub = (dt.hour-9)*3600+(dt.minute-20)*60+dt.second #以9:20:00當基準點來算過了幾秒
		subTime.append(sub)
	fh.close()
	return subTime	
import matplotlib.pyplot as py
endpoint = range(0,12000,1000)
subTime = findSubTimes('midterm2.csv')	
print(subTime)
# n,bins,patches = py.hist(subTime,bins = range(0,12000,1000))
# print(n) #每個區間有幾個點
# print(bins) #區間
py.hist(subTime,bins = endpoint ,facecolor ="gray",edgecolor ="black") #bins 切幾個長條
py.ylim(0,120)
py.xlim(0,11000)
py.xlabel('Submission Time')
py.ylabel('Frequency')
py.title('Histogram of Submission Time')
py.show()