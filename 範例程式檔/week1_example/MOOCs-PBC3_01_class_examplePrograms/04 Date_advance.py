class Date:
  doubleDigit = False

  @staticmethod
  def setDoubleDigit(dd):
    Date.doubleDigit = dd

  def isValidDate(self): # the invoker is a Date object
    if (1 <= self.year <= 3000) and (1 <= self.month <= 12):
      daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if self.isLeap() == True:
      daysInMonth[1] = 29
    if 1 <= self.day <= daysInMonth[self.month - 1]:
      return True
    return False 

  def toString(self):
    if Date.doubleDigit == False:
      return str(self.year) + "/" + str(self.month) + "/" + str(self.day)
    else:
      dateStr = str(self.year) + "/"
      dateStr += "0" + str(self.month) if self.month < 10 else str(self.month)
      dateStr += "/"
      dateStr += "0" + str(self.day) if self.day < 10 else str(self.day)
      return dateStr

  def isLeap(self):
    return isLeap(self.year)

  def isLaterThan(self, aDate):
    if self.year > aDate.year:
      return True
    elif self.year == aDate.year:
      if self.month > aDate.month:
        return True
      elif self.month == aDate.month:
        if self.day > aDate.day:
          return False
    return True
          
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

  def __str__(self):
    return self.toString()
    


    
def isLeap(year):
  if year % 400 == 0:
    return True
  elif (year % 4 == 0) and (year % 100 != 0):
    return True
  else:
    return False

def strToDate(birthday): # birthday is a yyyy/mm/dd string
  d = Date()
  year, month, day = birthday.split("/")
  d.year = int(year)
  d.month = int(month)
  d.day = int(day)
  return d

def printBdayDict(bdDict):
  for p in bdDict.keys():
    b = bdDict[p]
    print(p + " was born at " + b.toString())


    

	
	
d = Date(2018, 4, 5)
print(d.toString())

Date.setDoubleDigit(True)

d2 = Date(2018, 4, 5)
print(d2.toString())

