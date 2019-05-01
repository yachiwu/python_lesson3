import matplotlib.pyplot as py
import csv,datetime

#打開檔案
f = open('ubike.csv','r')
bike = {} #紀錄在公館站二號捷運出口每個時間點(0~1am,1~2am...有幾台車可以借)
capacity = {} #紀錄在公館站二號捷運出口每個時間點(0~1am,1~2am...總共有幾個停車格)(同個站點停車格數量一樣)
count = {} #紀錄每段時間區間被記錄了幾次

for row in csv.DictReader(f):
	if row['station'] == 'Roosevelt & Xinsheng S. Intersection':
		time = datetime.datetime.strptime(row['time'],"%Y/%m/%d %H:%M")
		hour = time.hour #只取小時
		if hour not in bike:
			bike[hour] = int(row['bike'])#時間區間內的可借腳踏車數
			capacity[hour] = int(row['lot'])#時間區間內的總腳踏車數
			count[hour] = 1 #該段時間區間共有幾天(這裡每個時段ex. 0~1am一天記錄一次)
		else:
			bike[hour] += int(row['bike'])
			capacity[hour] += int(row['lot'])
			count[hour] += 1
f.close()				
time_seq = bike.keys() #時間區間清單
time_seq = sorted(time_seq)
avg = [] 
lot = []
print(time_seq)
for k in time_seq:
	avg.append(float(bike[k])/count[k])
	lot.append(float(capacity[k])/count[k])
py.plot(time_seq,lot,label = 'capacity',marker='o')#畫出每個時段的總車位數
py.plot(time_seq,avg,label = 'Average',marker='o')#畫出每個時段的平均可借車位
py.xlabel('time(hr)')
py.ylabel('bike number can use')
py.xticks(range(24))
py.ylim(0,120)
py.legend(loc='upper right')
py.title('Roosevelt & Xinsheng S. Intersection bike analysis')
py.show()