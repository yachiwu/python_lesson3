#區段時間紀錄
class Time:
	def __init__(self,hour,minute,second): #初始化
		self.hour = hour
		self.minute = minute
		self.second = second
	def toString(self): #將時間轉為str
		return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
	def isLaterThan(self,time): #判斷時間time1  繳交時間>=time1
		if self.hour > time.hour:
			return True
		elif self.hour == time.hour:
			if self.minute > time.minute:
				return True
			elif self.minute == time.minute:
				if self.second >= time.second:
					return 	True
		return False	
	def isEarlyThan(self,time): #判斷時間time1  繳交時間<=time2
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
	return 	t
#讀取midterm2的資料
data = [] #儲存midterm2裡面的資料
with open('midterm2.csv','r',encoding ='cp950') as f:
	for line in f:
		if 'SubmissionID,StudentID,Problem,Status,Score,CodeLength,SubmissionTime' in line:
			continue
		submissionid,studentid,problem,status,score,codelenth,sunmissiontime = line.strip().split(',')
		data.append([submissionid,studentid,problem,status,score,codelenth,sunmissiontime])
	# print(data)	
#輸入欲查詢的繳交時間 ex 10:00 ~ 12:00	
time1 = input(' time1 -hh/mm/ss ')		
time1= strToTime(time1)		
print(time1.toString())
time2 = input(' time2 -hh/mm/ss ')		
time2 = strToTime(time2)	
print(time2.toString())	
#查詢data中繳交時間位於time1到time2之間的資料 並將資料存放在data_analysis中
data_analysis = [] #存放在time1到time2裡面的資料
for d in data:
	datatime = strToTime(d[6]) #將data資料中每一個時間轉匯為time object
	# print(datatime.toString())
	if datatime.isLaterThan(time1)==True and datatime.isEarlyThan(time2) == True:
	#如果datatime在time1到time2期間(包含time1 time2)的話就將datatime及他的資料加入到data_analysis中
		data_analysis.append([d[2],d[3]])
print(data_analysis) #印出在time1到time2期間的資料	
#重複產生submission物件來存放答案
submissiondata = []
for i in range(1,5):
	submission = {
	'problem' : i,
	'Accepted' : 0,
	'Compile Error' :0,
	'Runtime Error' :0,
	'Time Limit Exceed':0,
	'Wrong Answer' :0
	}
	submissiondata.append(submission)
# print(submissiondata)	
for d in data_analysis: #將問題及在問題中的錯誤進行統整
	for subdata in submissiondata:
		if int(d[0]) == subdata['problem']:
			subdata[d[1]]+=1
print(submissiondata)			
str_ans = ''
for ans in submissiondata:
	str_ans+= str(ans['Accepted'])+' '+str(ans['Compile Error'])+' '+str(ans['Runtime Error'])+' '+str(ans['Time Limit Exceed'])+' '+str(ans['Wrong Answer'])+';'
print(str_ans)
