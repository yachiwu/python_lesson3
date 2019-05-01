#輸入生日的class範例 
#在Date的class裡加入function
class Date:
	def isValidDate(self): #bDay is a Date object
		if (1<=self.year<=3000) and (1<=self.month<=12):
			daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
			if isLeap(self.year) == True:
				daysInMonth[1] = 29
			if 1<=self.day<=daysInMonth[self.month-1]:
				return True
		return False
	def isLeap(self):
		return isLeap(self.year)	
	def toString(self):
		return str(self.year)+'/'+str(self.month)+'/'+str(self.day)
			

	
	
def isLeap(year):
	if year %400 == 0:
		return True
	elif (year %4 ==0) and (year % 100 != 0):
		return True
	else:
		return False

def strToDate(birthday):
	d = Date()
	year,month,day = birthday.split("/")
	d.year = int(year)
	d.month = int(month)
	d.day = int(day)
	return d			

def printBdayDict(bdDict):
		for p in bdDict.keys():
			b = bdDict[p] #b是date物件
			print(p + ' was born '+ b.toString())

bdDict = dict()
while True:
	name = input('name : ')
	if (name == ""):
		break
	birthday = input('birthday yyyy/mm/dd: ')
	birthday = strToDate(birthday)	 #現在birthday 是一個object
	if birthday.isValidDate() == True:
		bdDict[name] = birthday	
	else:
		print('bad date')
	if birthday	=="":
		break
# print(bdDict)	
printBdayDict(bdDict)	

