class Date:
  pass
  
def isLeap(year):
  if year % 400 == 0:
    return True
  elif (year % 4 == 0) and (year % 100 != 0):
    return True
  else:
    return False

def isValidDate(bDay): # bDay is a Date object
  if (1 <= bDay.year <= 3000) and (1 <= bDay.month <= 12):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(bDay.year) == True:
      daysInMonth[1] = 29
    if 1 <= bDay.day <= daysInMonth[bDay.month - 1]:
      return True
  return False 

def strToDate(birthday): # birthday is a yyyy/mm/dd string
  d = Date()
  year, month, day = birthday.split("/")
  d.year = int(year)
  d.month = int(month)
  d.day = int(day)
  return d
  
def toString(bDay): # bDay is a Date object
  return str(bDay.year) + "/" + str(bDay.month) + "/" + str(bDay.day)
  
def printBdayDict(bdDict):
  for p in bdDict.keys():
    b = bdDict[p]
    print(p + " was born at " + toString(b))


    

	
	

bdDict = dict()

while True:
  name = input("name: ")
  if name == "":
    break
    
  birthday = input("birthday (yyyy/mm/dd): ")
  birthday = strToDate(birthday)

  if isValidDate(birthday) == True:
    bdDict[name] = birthday
  else:
    print("bad date!")

  if birthday == "":
    break  

print(bdDict)
printBdayDict(bdDict)