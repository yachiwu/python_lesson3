#輸入生日的class範例
#判斷正確性
# 1. 判斷是否為閏年
def isLeap(year):
	if year % 400 ==0:
		return True
	elif (year % 4==0 ) and (year % 100 !=0):
		return True
	else:
		return False
# 2. 檢查日期合理性
def isValidDate(birthday):	#birthday格式 yyyy/mm/dd
	year,month,day = birthday.split('/')
	year = int(year)
	month = int(month)
	day = int(day)
	if (1<=year<=3000) and (1<=month<=12):
		daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
		if isLeap(year) == True:
			daysInMonth[1] = 29
		if 1<=day<=daysInMonth[month-1]:
			return True
	return False			
bdDict = dict()
while True:
	name = input('name: ')
	if name == "":
		break
	birthday = input('birthday (yyyy/mm/dd) : ')
	if isValidDate(birthday) == True:
		bdDict[name] = birthday
	else:
		print('wrong date')	
	if birthday == "":
		break	
print(bdDict)			

