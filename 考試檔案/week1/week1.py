#區段時間紀錄
class Time:
	def __init__(self,hour,minute,second):
		self.hour = hour
		self.minute = minute
		self.second = second
	def toString(self):
		return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
	def isLaterThan(self,time): #判斷時間time1  時間>=time1
		if self.hour > time.hour:
			return True
		elif self.hour == time.hour:
			if self.minute > time.minute:
				return True
			elif self.minute == time.minute:
				if self.second >= time.second:
					return 	True
		return False	
	def isEarlyThan(self,time): #判斷時間time1  時間>=time1
		if self.hour < time.hour:
			return True
		elif self.hour == time.hour:
			if self.minute < time.minute:
				return True
			elif self.minute == time.minute:
				if self.second <= time.second:
					return 	True
		return False			

def strToTime(time):
	hour,minute,second = time.split(":")
	t = Time(int(hour),int(minute),int(second))
	# t.hour = int(hour)
	# t.minute = int(minute)
	# t.second = int(second)
	return 	t

data = [] #儲存midterm2裡面的資料
data_analysis = [] #存放在time1 time2 裡面的資料
#存放問題一錯誤的字典
dict1 = {
	'Accepted' : 0,
	'Compile Error' :0,
	'Runtime Error' :0,
	'Time Limit Exceed':0,
	'Wrong Answer' :0
	} 
dict2 = {
	'Accepted' : 0,
	'Compile Error' :0,
	'Runtime Error' :0,
	'Time Limit Exceed':0,
	'Wrong Answer' :0
	} 
dict3 = {
	'Accepted' : 0,
	'Compile Error' :0,
	'Runtime Error' :0,
	'Time Limit Exceed':0,
	'Wrong Answer' :0
	} 
dict4 = {
	'Accepted' : 0,
	'Compile Error' :0,
	'Runtime Error' :0,
	'Time Limit Exceed':0,
	'Wrong Answer' :0
	} 	
with open('midterm2.csv','r',encoding ='cp950') as f:
	for line in f:
		if 'SubmissionID,StudentID,Problem,Status,Score,CodeLength,SubmissionTime' in line:
			continue
		submissionid,studentid,problem,status,score,codelenth,sunmissiontime = line.strip().split(',')
		data.append([submissionid,studentid,problem,status,score,codelenth,sunmissiontime])
	print(data)	
time1 = input(' time1 -hh/mm/ss ')		
time1= strToTime(time1)		
print(time1.toString())
time2 = input(' time2 -hh/mm/ss ')		
time2 = strToTime(time2)	
print(time2.toString())	
for d in data:
	datatime = strToTime(d[6]) #將資料中的時間轉匯為time
	# print(datatime.toString())
	if datatime.isLaterThan(time1)==True and datatime.isEarlyThan(time2) == True:
		data_analysis.append([d[2],d[3]])
print(data_analysis)	

for d in data_analysis:
	if d[0] == '1':
		if d[1] in dict1:
			dict1[d[1]]+=1
	elif d[0] == '2':
		if d[1] in dict2:
			dict2[d[1]]+=1
	elif d[0] == '3':
		if d[1] in dict3:
			dict3[d[1]]+=1
	elif d[0] =='4'	:
		if d[1] in dict4:
			dict4[d[1]]+=1
print(dict1)
print(dict2)
print(dict3)
print(dict4)




# print(time1.toString())
# atime = Time(9,00,00)
# print(atime.isLaterThan(time1))
